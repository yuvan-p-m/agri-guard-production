from fastapi import APIRouter, Depends, File, UploadFile, HTTPException, status, Query, Request
import os
from datetime import datetime
from typing import Optional

from db.firestore_db import create_disease_record, get_disease_records, save_prediction_to_firestore
from schemas.common import DiseaseResponse
from core.security import get_current_user
from core.logger import get_logger
from services.ai_localization import get_disease_display_name, get_crop_display_name
from services.gemini_service import (
    diagnose_crop_disease,
    GeminiError,
    GeminiConfigError,
    GeminiTimeoutError,
    GeminiAPIError,
    GeminiParseError
)

logger = get_logger(__name__)
router = APIRouter(prefix="/disease", tags=["Disease Detection"])


async def get_optional_user(request: Request) -> dict:
    auth_header = request.headers.get("Authorization")
    if not auth_header:
        return {"user_id": "anonymous_farmer"}
    try:
        from fastapi.security import HTTPAuthorizationCredentials
        token = auth_header.replace("Bearer ", "").strip()
        user = await get_current_user(HTTPAuthorizationCredentials(scheme="Bearer", credentials=token))
        return user if user else {"user_id": "anonymous_farmer"}
    except Exception:
        return {"user_id": "anonymous_farmer"}


@router.post("/predict")
async def predict_disease(
    file: UploadFile = File(...),
    language: Optional[str] = Query(None),
    request: Request = None
):
    """
    Predict crop disease from leaf image using Google Gemini Vision AI (sole inference engine).
    Saves prediction and history records to Firestore.
    """
    if not file or not file.filename:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No image file provided for crop diagnosis."
        )

    try:
        contents = await file.read()
    except Exception as read_err:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Failed to read uploaded image file: {read_err}"
        )

    if not contents or len(contents) < 64:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Uploaded image file is empty or corrupted."
        )

    user = await get_optional_user(request) if request else {"user_id": "anonymous_farmer"}
    farmer_id = user.get("user_id", "anonymous_farmer")
    req_lang = (
        language
        or (request.query_params.get("language") if request else None)
        or (request.headers.get("x-language") if request else None)
        or "en"
    )

    # Save uploaded image to disk for record-keeping
    os.makedirs("uploads", exist_ok=True)
    timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    image_path = f"uploads/{farmer_id}_{timestamp}.jpg"
    try:
        with open(image_path, "wb") as f:
            f.write(contents)
    except Exception as io_err:
        logger.warning(f"Notice: could not save uploaded image to disk: {io_err}")

    # Call Gemini AI disease diagnosis service (sole inference path)
    try:
        prediction = diagnose_crop_disease(contents, language=req_lang)
    except GeminiConfigError as ce:
        logger.error(f"Gemini configuration error: {ce}")
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="AI crop diagnosis service is not configured (GEMINI_API_KEY missing). Please set GEMINI_API_KEY."
        )
    except GeminiTimeoutError as te:
        logger.error(f"Gemini timeout error: {te}")
        raise HTTPException(
            status_code=status.HTTP_504_GATEWAY_TIMEOUT,
            detail="AI crop diagnosis request timed out. Please try again."
        )
    except GeminiAPIError as ae:
        logger.error(f"Gemini upstream API error: {ae}")
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail=f"AI diagnosis service error: {str(ae)}"
        )
    except GeminiParseError as pe:
        logger.error(f"Gemini response parsing error: {pe}")
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail="Failed to parse AI crop diagnosis response."
        )
    except ValueError as ve:
        logger.warning(f"Image validation error: {ve}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(ve)
        )
    except Exception as e:
        logger.error(f"Unexpected error during crop diagnosis: {e}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Crop diagnosis failed: {str(e)}"
        )

    # Early termination guard: If image is not a valid plant leaf
    if prediction.get("status") == "invalid_leaf" or not prediction.get("is_plant_leaf", True):
        logger.info(f"Invalid leaf detected in predict_disease: {prediction.get('message')}")
        return {
            "disease": prediction.get("disease", "No Crop Leaf Detected"),
            "confidence": float(prediction.get("confidence", 0.0)),
            "status": "invalid_leaf",
            "message": prediction.get("message", "The uploaded photo does not appear to contain a valid crop leaf. Please upload a clear photo of a plant leaf."),
            "provider": "gemini",
            "model_used": prediction.get("model_used", "gemini-2.5-flash"),
            "reasoning": prediction.get("reasoning", ""),
            "progression_risk": None,
            "pesticide_recommendation": None,
            "treatment": None,
            "sensor_snapshot": None,
            "weather_snapshot": None,
        }

    disease_name = prediction["disease"]
    confidence = float(prediction["confidence"])
    
    # Save to Firestore collection "predictions"
    prediction_firestore_data = {
        "userId": str(farmer_id),
        "disease": disease_name,
        "confidence": confidence,
        "imageUrl": image_path,
        "status": "success",
        "provider": "gemini"
    }
    save_prediction_to_firestore(prediction_firestore_data)
    
    # Save to Firestore collection "disease_records" for history tab
    record_data = {
        "farmer_id": str(farmer_id),
        "image_path": image_path,
        "predicted_disease": disease_name,
        "confidence": confidence,
        "severity": prediction.get("severity", "medium"),
        "treatment": f"Apply recommended protocol for {disease_name.replace('___', ' ').replace('_', ' ')}",
        "pesticide_dose": "2.5ml per liter water"
    }
    
    record = create_disease_record(record_data)
    doc_id = str(record.get("id"))
    logger.info(f"Prediction saved to Firestore: {doc_id} - {disease_name}")

    # Disease Progression Risk Assessment via Gemini AI
    from services.sensor_service import fetch_live_sensor_data
    from services.gemini_service import get_disease_progression_risk
    from api.weather import WeatherService

    sensor_data = fetch_live_sensor_data() or {}
    try:
        weather_data = WeatherService.fetch_weather() or {}
    except Exception as w_err:
        logger.warning(f"Weather fetch notice during disease prediction: {w_err}")
        weather_data = {}

    try:
        progression_risk = get_disease_progression_risk(
            disease_name=disease_name,
            confidence=confidence,
            sensor_data=sensor_data,
            weather_data=weather_data,
            language=req_lang
        )
    except Exception as err:
        logger.error(f"Error computing disease progression risk: {err}")
        progression_risk = {
            "risk": "Risk Assessment Unavailable",
            "message": "Unable to calculate progression risk at this time.",
            "treatment": None,
            "pesticide_recommendation": None
        }

    localized_disease = get_disease_display_name(disease_name, req_lang)

    return {
        "disease": disease_name,
        "crop": prediction.get("crop", ""),
        "localized_disease": localized_disease,
        "disease_display": localized_disease,
        "confidence": confidence,
        "status": "success",
        "is_healthy": prediction.get("is_healthy", False),
        "severity": prediction.get("severity", "medium"),
        "pathogen_type": prediction.get("pathogen_type", "None"),
        "symptoms": prediction.get("symptoms", []),
        "reasoning": prediction.get("reasoning", ""),
        "provider": "gemini",
        "model_used": prediction.get("model_used", "gemini-2.5-flash"),
        "disease_prediction": {
            "disease": disease_name,
            "localized_disease": localized_disease,
            "confidence": confidence,
            "status": "success",
            "provider": "gemini"
        },
        "progression_risk": progression_risk,
        "pesticide_recommendation": (
            progression_risk.get("pesticide_recommendation")
            or progression_risk.get("treatment")
            if isinstance(progression_risk, dict) else None
        ),
        "treatment": (
            progression_risk.get("treatment")
            or progression_risk.get("pesticide_recommendation")
            if isinstance(progression_risk, dict) else None
        ),
        "sensor_snapshot": sensor_data,
        "weather_snapshot": weather_data
    }

@router.get("/history")
async def disease_history(
    current_user: dict = Depends(get_current_user)
):
    """Get farmer's disease history from Firestore"""
    
    farmer_id = current_user.get("user_id")
    records = get_disease_records(farmer_id=farmer_id, limit=30)
    
    return {
        "total": len(records),
        "records": [
            {
                "id": r.get("id"),
                "disease": r.get("predicted_disease") or r.get("disease"),
                "confidence": r.get("confidence"),
                "timestamp": r.get("timestamp"),
                "image_path": r.get("image_path")
            }
            for r in records
        ]
    }


from pydantic import BaseModel

class ProgressionRiskRequest(BaseModel):
    disease_name: str
    confidence: float
    language: Optional[str] = "en"
    location: Optional[str] = ""

@router.post("/progression-risk")
async def get_progression_risk_endpoint(
    payload: ProgressionRiskRequest,
    request: Request = None
):
    """
    Re-evaluate disease progression risk and precision pesticide treatment
    in real time for the farmer's selected language (supports all 25 languages).
    """
    from services.sensor_service import fetch_live_sensor_data
    from services.gemini_service import get_disease_progression_risk
    from api.weather import WeatherService

    sensor_data = fetch_live_sensor_data() or {}
    try:
        weather_data = WeatherService.fetch_weather() or {}
    except Exception as w_err:
        logger.warning(f"Weather fetch notice during disease progression risk: {w_err}")
        weather_data = {}

    req_lang = (
        payload.language
        or (request.query_params.get("language") if request else None)
        or (request.headers.get("x-language") if request else None)
        or "en"
    )

    try:
        progression_risk = get_disease_progression_risk(
            disease_name=payload.disease_name,
            confidence=payload.confidence,
            sensor_data=sensor_data,
            weather_data=weather_data,
            location=payload.location or "",
            language=req_lang
        )
    except Exception as err:
        logger.error(f"Error computing disease progression risk: {err}")
        progression_risk = {
            "risk": "Risk Assessment Unavailable",
            "message": "Unable to calculate progression risk at this time.",
            "treatment": None,
            "pesticide_recommendation": None
        }

    localized_disease = get_disease_display_name(payload.disease_name, req_lang)

    return {
        "status": "success",
        "disease": payload.disease_name,
        "localized_disease": localized_disease,
        "disease_display": localized_disease,
        "confidence": payload.confidence,
        "progression_risk": progression_risk,
        "pesticide_recommendation": (
            progression_risk.get("pesticide_recommendation")
            or progression_risk.get("treatment")
            if isinstance(progression_risk, dict) else None
        ),
        "treatment": (
            progression_risk.get("treatment")
            or progression_risk.get("pesticide_recommendation")
            if isinstance(progression_risk, dict) else None
        ),
        "sensor_snapshot": sensor_data,
        "weather_snapshot": weather_data
    }

