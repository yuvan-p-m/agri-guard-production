import logging
import sys
from pathlib import Path

from typing import Optional
from fastapi import FastAPI, File, UploadFile, HTTPException, status, Request, Query
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

# Resolve backend directory and load backend/.env reliably regardless of CWD
BACKEND_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BACKEND_DIR / ".env")

# Add app directory and backend root to path for imports
sys.path.insert(0, str(Path(__file__).parent))
sys.path.insert(0, str(BACKEND_DIR))

from core.logger import setup_logging
from core.config import settings
from core.firebase import init_firebase, is_firebase_initialized

# Import API routes and services
from api import auth, alerts, disease, crop, sensors, weather, risk, feedback, pesticides, history, marketplace, predictive
from db.firestore_db import save_prediction_to_firestore

setup_logging()
logger = logging.getLogger(__name__)

app = FastAPI(
    title="SIH Agri-Smart API",
    description="AI-powered crop disease detection & recommendation system with Firebase Integration",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register API routes across root, /api/v1, and /api prefixes
api_routers = [
    auth.router,
    auth.root_router,
    alerts.router,
    disease.router,
    crop.router,
    sensors.router,
    weather.router,
    risk.router,
    feedback.router,
    pesticides.router,
    history.router,
    marketplace.router,
    predictive.router
]

for r in api_routers:
    app.include_router(r)
    app.include_router(r, prefix="/api/v1")
    app.include_router(r, prefix="/api")


@app.get("/health")
@app.get("/api/v1/health")
@app.get("/api/health")
def health_check():
    """Health check endpoint"""
    return {
        "status": "ok",
        "message": "API is running",
        "version": "1.0.0",
    }


@app.get("/model/status")
@app.get("/api/v1/model/status")
@app.get("/api/model/status")
def model_status():
    """Returns status of AI diagnosis engine (Google Gemini Vision AI)"""
    import os
    api_key_configured = bool(os.getenv("GEMINI_API_KEY", "").strip())
    model_name = os.getenv("GEMINI_MODEL", "gemini-2.5-flash").strip() or "gemini-2.5-flash"
    return {
        "model_loaded": api_key_configured,
        "model_id": model_name,
        "status": "ready" if api_key_configured else "unconfigured",
        "provider": "gemini",
        "api_reachable": True
    }


@app.get("/crop-recommendations")
@app.get("/api/v1/crop-recommendations")
@app.get("/api/crop-recommendations")
async def crop_recommendations_root_endpoint(
    request: Request,
    location: str = "getting location",
    language: Optional[str] = Query(None)
):
    """
    Part 2: GET /crop-recommendations?location=...
    Internally: fetches weather -> fetches sensor snapshot -> calls Gemini -> returns parsed JSON
    """
    from api.crop import execute_crop_recommendations
    req_lang = language or request.query_params.get("language") or request.headers.get("x-language") or "en"
    return await execute_crop_recommendations(location, language=req_lang)


@app.get("/")
def root():
    """Root endpoint - API info"""
    return {
        "name": "SIH Agri-Smart API",
        "version": "1.0.0",
        "description": "AI-powered crop disease detection & recommendation system (Gemini AI Vision Engine)",
        "docs": "/docs",
        "firebase_active": is_firebase_initialized(),
        "ai_engine": "Google Gemini Vision AI",
        "endpoints": {
            "auth": "/auth",
            "disease": "/disease",
            "crop": "/crop",
            "sensors": "/sensors",
            "weather": "/weather",
            "risk": "/risk",
            "feedback": "/feedback",
            "pesticides": "/pesticides",
            "alerts": "/alerts",
            "history": "/history"
        }
    }


@app.on_event("startup")
async def startup():
    logger.info("SIH Agri-Smart API starting...")
    init_firebase()
    if is_firebase_initialized():
        logger.info("Firebase Admin initialized successfully.")
    else:
        logger.info("Firebase Admin running with mock DB fallback.")
    
    # Load Crop Random Forest model ONCE at startup
    try:
        from services.crop_model_service import CropRandomForestService
        CropRandomForestService.load_model()
    except Exception as e:
        logger.error(f"Startup warning: Crop Random Forest model failed to load: {e}")

    # Start automated 4 daily SMS cron scheduler (APScheduler)
    try:
        from scheduler import start_scheduler
        start_scheduler()
        logger.info("Fast2SMS 4-times daily cron scheduler started.")
    except Exception as e:
        logger.warning(f"SMS scheduler startup notice: {e}")


@app.post("/predict")
@app.post("/api/v1/predict")
@app.post("/api/predict")
@app.post("/disease/predict")
@app.post("/api/v1/disease/predict")
@app.post("/api/disease/predict")
async def predict_endpoint(
    request: Request,
    file: UploadFile = File(...),
    language: Optional[str] = Query(None)
):
    """
    POST /predict endpoint
    Accepts multipart image upload ('file'), runs Google Gemini Vision AI diagnosis,
    saves record to Firestore 'predictions' collection, and returns structured diagnosis JSON.
    """
    from api.disease import predict_disease
    return await predict_disease(file=file, language=language, request=request)


@app.on_event("shutdown")
async def shutdown():
    logger.info("SIH Agri-Smart API shutting down...")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )

