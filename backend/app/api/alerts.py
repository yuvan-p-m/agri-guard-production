import logging
from typing import Optional, List, Dict, Any
from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel

from core.security import get_current_user
from core.logger import get_logger
from sms_service import send_sms_detailed, validate_and_clean_indian_mobile

logger = get_logger(__name__)
router = APIRouter(prefix="/alerts", tags=["SMS & Alerts"])


class SubscribePayload(BaseModel):
    phone: str
    crop: Optional[str] = "Citrus (Orange / Lemon)"
    alert_types: Optional[List[str]] = ["disease_risk", "weather_warning"]


class WeatherAlertPayload(BaseModel):
    phone: str
    alert_message: str


class TestSmsPayload(BaseModel):
    uid: Optional[str] = None
    phone: Optional[str] = None
    location: Optional[str] = "Nagpur"
    name: Optional[str] = "Farmer Partner"


@router.post("/subscribe")
async def subscribe_to_alerts(payload: SubscribePayload):
    """
    Subscribes a farmer's mobile number to automatic micro-climate & disease advisory alerts.
    Dispatches a confirmation welcome SMS.
    """
    clean_phone = validate_and_clean_indian_mobile(payload.phone)
    if not clean_phone:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Invalid Indian mobile number '{payload.phone}'. Must be a 10-digit number starting with 6, 7, 8, or 9."
        )

    crop = payload.crop or "Citrus (Orange / Lemon)"
    alert_types = payload.alert_types or ["disease_risk", "weather_warning"]
    welcome_msg = f"Welcome to AgriGuard! Your farm is now connected for {crop} alerts. Stay informed, farm smarter."

    sms_res = send_sms_detailed(clean_phone, welcome_msg)

    return {
        "status": "subscribed",
        "phone": clean_phone,
        "crop": crop,
        "alert_types": alert_types,
        "sms_sent": sms_res.get("success", False),
        "message": "Subscription confirmed! SMS alert activated." if sms_res.get("success") else f"Subscribed, but SMS notice: {sms_res.get('message')}"
    }


@router.post("/send-weather-alert")
async def send_weather_alert(payload: WeatherAlertPayload):
    """
    Dispatches a specific live weather warning advisory to the farmer's registered phone.
    """
    clean_phone = validate_and_clean_indian_mobile(payload.phone)
    if not clean_phone:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Invalid Indian mobile number '{payload.phone}'. Must be a 10-digit number starting with 6, 7, 8, or 9."
        )

    message = f"WEATHER ALERT: {payload.alert_message.strip()}"
    res = send_sms_detailed(clean_phone, message)

    if res.get("success"):
        logger.info(f"Weather alert delivered to farmer {clean_phone}")
        return {"success": True, "status": "sent", "phone": clean_phone, "message": message}

    # Map error types to appropriate HTTP status codes
    error_type = res.get("error_type")
    err_msg = res.get("message", "Failed to dispatch SMS")

    if error_type == "config_error":
        raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail=err_msg)
    elif error_type == "validation_error":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=err_msg)
    elif error_type == "network_error":
        raise HTTPException(status_code=status.HTTP_504_GATEWAY_TIMEOUT, detail=err_msg)
    else:
        raise HTTPException(status_code=status.HTTP_502_BAD_GATEWAY, detail=f"Fast2SMS error: {err_msg}")


@router.post("/send-test-sms")
async def send_test_sms_endpoint(payload: TestSmsPayload):
    """
    Interactive SMS Demo endpoint: builds real-time micro-climate & sensor summary and dispatches to mobile.
    """
    from db.firestore_db import get_user_by_id

    phone = payload.phone
    name = payload.name or "Farmer Partner"
    location = payload.location or "Nagpur"

    if payload.uid:
        user_doc = get_user_by_id(payload.uid)
        if user_doc:
            phone = user_doc.get("phone") or phone
            name = user_doc.get("full_name") or user_doc.get("name") or name
            location = user_doc.get("location") or location

    if not phone:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Farmer phone number not found. Please update phone number in profile."
        )

    clean_phone = validate_and_clean_indian_mobile(phone)
    if not clean_phone:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Invalid Indian phone number '{phone}'. Must be a 10-digit number starting with 6, 7, 8, or 9."
        )

    # Fetch live weather for location
    try:
        from weather_service import get_weather
        weather_res = get_weather(location)
        temp = weather_res.get("temp", 28)
        humidity = weather_res.get("humidity", 74)
        rain_val = weather_res.get("rain", "No")
        irrigation = weather_res.get("irrigation", "Morning")
    except Exception:
        temp = 28
        humidity = 74
        rain_val = "No"
        irrigation = "Morning"

    # Fetch live IoT Hardware Sensor Telemetry if available
    sensor_info_str = ""
    try:
        from services.sensor_service import fetch_live_sensor_data
        live_sensors = fetch_live_sensor_data() or {}
        if live_sensors and "ph" in live_sensors:
            raw_ph = float(live_sensors.get("ph", 6.5))
            raw_moist = float(live_sensors.get("moisture", 42.0))
            clean_ph = round(raw_ph, 1) if raw_ph <= 14 else 6.8
            clean_moist = round(raw_moist) if raw_moist <= 100 else 42
            sensor_info_str = f" Soil: {clean_moist}%, pH {clean_ph}."
    except Exception as sens_err:
        logger.debug(f"Sensor read notice: {sens_err}")

    message = f"Good Morning {name}! Today: Temp {temp}C, Humidity {humidity}%, Rain: {rain_val}.{sensor_info_str} Best irrigation time: {irrigation}."

    res = send_sms_detailed(clean_phone, message)

    if res.get("success"):
        return {"success": True, "status": "sent", "phone": clean_phone, "message": message}

    error_type = res.get("error_type")
    err_msg = res.get("message", "Failed to dispatch SMS")

    if error_type == "config_error":
        raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail=err_msg)
    elif error_type == "validation_error":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=err_msg)
    elif error_type == "network_error":
        raise HTTPException(status_code=status.HTTP_504_GATEWAY_TIMEOUT, detail=err_msg)
    else:
        raise HTTPException(status_code=status.HTTP_502_BAD_GATEWAY, detail=f"Fast2SMS error: {err_msg}")


@router.get("/message-templates")
async def get_message_templates(
    current_user: dict = Depends(get_current_user)
):
    templates = {
        "morning_weather": "Good Morning {name}! Today: Temp {temp}C, Humidity {humidity}%, Rain: {rain}. Best irrigation time: {irrigation}.",
        "soil_sensor": "Sensor Update for {crop} farm: Moisture: {moisture}%, pH: {ph}, Nitrogen: {nitrogen}ppm. Action: {action}",
        "midday_weather": "Afternoon {name}: Temp {temp}C, Wind {wind}km/h. {task_tip}",
        "evening_tip": "Evening Tip for {crop} farmers: {tip} Tomorrow: {forecast}."
    }
    return {"templates": templates, "gateway": "Fast2SMS"}
