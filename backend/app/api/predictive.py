"""
Predictive Intelligence API Router
Endpoint for outbreak risk forecasting combining IoT, weather, seasonal, and community signals.
"""

from typing import Optional, Dict, Any, List
from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, Field

from services.predictive_service import compute_predictive_outbreak_risk
from core.logger import get_logger

logger = get_logger(__name__)

router = APIRouter(prefix="/predictive", tags=["Predictive Intelligence"])


class SensorDataPayload(BaseModel):
    N: Optional[float] = Field(default=120.0, description="Nitrogen level in mg/kg")
    P: Optional[float] = Field(default=55.0, description="Phosphorus level in mg/kg")
    K: Optional[float] = Field(default=175.0, description="Potassium level in mg/kg")
    moisture: Optional[float] = Field(default=52.0, description="Soil moisture %")
    temperature: Optional[float] = Field(default=27.0, description="Air temperature °C")
    humidity: Optional[float] = Field(default=65.0, description="Relative humidity %")
    pH: Optional[float] = Field(default=6.5, description="Soil pH value")


class OutbreakRiskRequest(BaseModel):
    farmer_id: Optional[str] = Field(default="1", description="Farmer ID")
    lat: float = Field(default=21.1458, description="Latitude")
    lon: float = Field(default=79.0882, description="Longitude")
    crop: str = Field(default="Tomato", description="Primary crop cultivated")
    sensor_data: SensorDataPayload = Field(..., description="Current telemetry readings from IoT sensors")


class CommunityThreatsModel(BaseModel):
    report_count: int
    diseases_reported: List[str]
    nearest_outbreak_km: float


class PredictedOutbreakItem(BaseModel):
    disease: str
    probability: float
    days_until_window: int


class FiveDayRiskItem(BaseModel):
    date: str
    risk_score: float
    risk_level: str


class OutbreakRiskResponse(BaseModel):
    overall_risk_score: float
    risk_level: str
    soil_health_index: float
    weather_risk_score: float
    seasonal_risk_level: str
    community_threats: CommunityThreatsModel
    predicted_outbreaks: List[PredictedOutbreakItem]
    five_day_forecast: List[FiveDayRiskItem]
    recommended_actions: List[str]


@router.post("/outbreak-risk", response_model=OutbreakRiskResponse)
async def post_outbreak_risk(payload: OutbreakRiskRequest):
    """
    POST /api/predictive/outbreak-risk
    Predicts crop disease outbreak risks before they occur by fusing live IoT sensor data,
    hyperlocal 5-day weather forecasts, seasonal risk calendars, and nearby community threat reports.
    """
    try:
        sensor_dict = payload.sensor_data.model_dump()
        result = compute_predictive_outbreak_risk(
            farmer_id=payload.farmer_id or "1",
            lat=payload.lat,
            lon=payload.lon,
            crop=payload.crop or "Tomato",
            sensor_data=sensor_dict
        )
        return result
    except Exception as e:
        logger.error(f"Error computing outbreak risk prediction: {str(e)}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to generate predictive intelligence: {str(e)}"
        )
