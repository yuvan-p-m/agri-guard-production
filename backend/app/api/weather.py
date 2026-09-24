import os
import requests
from typing import Optional
from fastapi import APIRouter, Depends, HTTPException, status, Query, Request
from datetime import datetime, timedelta
from pathlib import Path
from dotenv import load_dotenv

BACKEND_DIR = Path(__file__).resolve().parent.parent.parent
load_dotenv(BACKEND_DIR / ".env")

from db.firestore_db import get_weather_cache, set_weather_cache, get_user_by_id, get_latest_sensor_reading
from core.security import get_current_user
from core.logger import get_logger
from services.ai_localization import (
    get_localized_weather_alerts,
    localize_weather_condition,
    localize_soil_moisture,
    SUPPORTED_LANGUAGES
)

logger = get_logger(__name__)

def _resolve_language(request: Optional[Request], query_lang: Optional[str]) -> str:
    lang = (query_lang or "").strip().lower()
    if not lang and request:
        lang = (request.headers.get("X-Language") or "").strip().lower()
    if lang in SUPPORTED_LANGUAGES:
        return lang
    return "en"

router = APIRouter(prefix="/weather", tags=["Weather Integration"])

WEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY") or os.getenv("WEATHER_API_KEY")

CITY_COORDINATES = {
    "getting location": {"lat": 21.1458, "lng": 79.0882, "state": "Maharashtra"},
    "Nashik": {"lat": 19.9975, "lng": 73.7898, "state": "Maharashtra"},
    "Coimbatore": {"lat": 11.0168, "lng": 76.9558, "state": "Tamil Nadu"},
    "Varanasi": {"lat": 25.3176, "lng": 82.9739, "state": "Uttar Pradesh"},
    "Ludhiana": {"lat": 30.9010, "lng": 75.8573, "state": "Punjab"},
    "Vijayawada": {"lat": 16.5062, "lng": 80.6480, "state": "Andhra Pradesh"}
}

class WeatherService:
    @staticmethod
    def get_city_coords(city_name: str) -> dict:
        clean = city_name.split("(")[0].strip() if city_name else "getting location"
        for key, info in CITY_COORDINATES.items():
            if key.lower() in clean.lower() or clean.lower() in key.lower():
                return info
        return {"lat": 21.1458, "lng": 79.0882, "state": "Maharashtra"}

    @staticmethod
    def reverse_geocode_osm(lat: float, lon: float) -> tuple:
        """
        Use OpenStreetMap (Nominatim) free reverse geocoding API to resolve
        hyper-accurate village, suburb, town, city, district and state names.
        """
        try:
            url = f"https://nominatim.openstreetmap.org/reverse?format=json&lat={lat}&lon={lon}&zoom=14&addressdetails=1"
            headers = {"User-Agent": "AgriGuard-App/1.0 (agri.health.assistant@gmail.com)"}
            res = requests.get(url, headers=headers, timeout=4)
            if res.status_code == 200:
                addr = res.json().get("address", {})
                place = (
                    addr.get("village") or
                    addr.get("suburb") or
                    addr.get("town") or
                    addr.get("city_district") or
                    addr.get("neighbourhood") or
                    addr.get("city") or
                    addr.get("county") or
                    addr.get("state_district")
                )
                city = addr.get("city") or addr.get("state_district") or addr.get("county") or ""
                state = addr.get("state") or addr.get("country") or "India"

                if place and city and place.lower() != city.lower():
                    clean_loc = f"{place}, {city}"
                elif place:
                    clean_loc = place
                elif city:
                    clean_loc = city
                else:
                    clean_loc = ""

                if clean_loc:
                    return clean_loc, state
        except Exception as e:
            logger.debug(f"OSM Nominatim reverse geocode notice: {e}")
        return "", ""

    @staticmethod
    def fetch_weather(lat: float = None, lon: float = None, city: str = "getting location", language: str = "en") -> dict:
        """
        Fetch live weather telemetry from OpenWeatherMap API using GPS coords or city fallback,
        and derive dynamic weather risk alerts.
        """
        if lat is None or lon is None:
            coords = WeatherService.get_city_coords(city)
            lat, lon = coords["lat"], coords["lng"]

        location_name = city.split("(")[0].strip() if city else "getting location"
        state_name = "India"
        api_key = os.getenv("OPENWEATHER_API_KEY") or os.getenv("WEATHER_API_KEY") or WEATHER_API_KEY

        # 1. Reverse Geocode via OpenStreetMap (Nominatim) for hyper-precise village / suburb / city name
        osm_loc, osm_state = WeatherService.reverse_geocode_osm(lat, lon)
        if osm_loc:
            location_name = osm_loc
        if osm_state:
            state_name = osm_state

        try:
            if api_key:
                logger.info(f"Fetching OpenWeatherMap forecast for coords: {lat}, {lon}")
                url = f"http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={api_key}&units=metric"
                response = requests.get(url, timeout=6)
                if response.status_code == 200:
                    data = response.json()
                    
                    if not osm_loc and data.get("city") and data["city"].get("name"):
                        raw_name = data["city"]["name"]
                        if "Saint Thomas Mount" in raw_name or "St. Thomas Mount" in raw_name:
                            location_name = "Chennai (St. Thomas Mount)"
                        else:
                            location_name = raw_name
                        country = data["city"].get("country", "")
                        state_name = country if country else "India"

                    first_item = data.get("list", [{}])[0]
                    main = first_item.get("main", {})
                    weather_cond = first_item.get("weather", [{}])[0]
                    wind = first_item.get("wind", {})

                    tempC = round(main.get("temp", 28), 1)
                    humidity = main.get("humidity", 75)
                    condition_desc = weather_cond.get("description", "partly cloudy").title()
                    wind_speed = round(wind.get("speed", 3.5) * 3.6, 1)
                    rain_mm = round(first_item.get("rain", {}).get("3h", 0), 1)

                    # Build 5-day daily forecast
                    forecast_list = []
                    seen_dates = set()
                    for item in data.get("list", []):
                        date_str = item["dt_txt"].split(" ")[0]
                        if date_str not in seen_dates and len(seen_dates) < 5:
                            seen_dates.add(date_str)
                            h = item["main"]["humidity"]
                            forecast_list.append({
                                "date": date_str,
                                "time": item["dt_txt"],
                                "temp": round(item["main"]["temp"], 1),
                                "temp_max": round(item["main"]["temp_max"], 1),
                                "temp_min": round(item["main"]["temp_min"], 1),
                                "humidity": h,
                                "condition": item["weather"][0]["description"].title(),
                                "rainfall_mm": round(item.get("rain", {}).get("3h", 0), 1),
                                "disease_risk": "High" if h > 75 else "Medium" if h > 60 else "Low",
                                "risk_reason": "High humidity favors fungal spore germination" if h > 75 else "Favorable microclimate"
                            })

                    return WeatherService._format_weather_response(
                        location=location_name,
                        state=state_name,
                        tempC=tempC,
                        condition=condition_desc,
                        humidity=humidity,
                        wind_speed=wind_speed,
                        rain_mm=rain_mm,
                        forecast_list=forecast_list,
                        language=language
                    )
        except Exception as e:
            logger.error(f"OpenWeatherMap fetch error: {str(e)}")

        return WeatherService._fallback_weather(lat, lon, location_name, language=language)

    @staticmethod
    def _format_weather_response(
        location: str,
        state: str,
        tempC: float,
        condition: str,
        humidity: int,
        wind_speed: float,
        rain_mm: float,
        forecast_list: list,
        language: str = "en"
    ) -> dict:
        rainfall_chance = min(98, max(5, humidity - 10 + int(rain_mm * 5)))
        risk_level = "Severe" if humidity >= 85 and tempC >= 25 else "High" if humidity >= 75 else "Moderate" if humidity >= 60 else "Low"
        leaf_wetness = round(max(2.0, min(14.0, (humidity / 100) * 12 + rain_mm)), 1)
        soil_moisture = localize_soil_moisture(pct=min(95, max(45, humidity - 5)), is_adequate=(humidity < 80), lang=language)

        loc_condition = localize_weather_condition(condition, language)
        alert_summary, dynamic_alerts = get_localized_weather_alerts(
            humidity=humidity,
            tempC=tempC,
            rain_chance=rainfall_chance,
            condition=condition,
            leaf_wetness=leaf_wetness,
            soil_moisture=soil_moisture,
            lang=language
        )

        localized_forecast = []
        for item in forecast_list:
            c = item.get("condition", "")
            localized_forecast.append({
                **item,
                "condition": localize_weather_condition(c, language),
                "risk_reason": alert_summary if language != "en" else item.get("risk_reason", "")
            })

        return {
            "location": location,
            "city": location,
            "state": state,
            "tempC": tempC,
            "condition": loc_condition,
            "raw_condition": condition,
            "humidity": humidity,
            "rainfallChance": rainfall_chance,
            "windSpeedKmH": wind_speed,
            "soilMoisture": soil_moisture,
            "fungalRiskLevel": risk_level,
            "leafWetnessHours": leaf_wetness,
            "alertSummary": alert_summary,
            "summary": alert_summary,
            "alerts": dynamic_alerts,
            "current": {
                "temp": tempC,
                "humidity": humidity,
                "condition": loc_condition,
                "wind_speed": wind_speed
            },
            "forecast": localized_forecast
        }

    @staticmethod
    def _fallback_weather(lat: float, lon: float, location_name: str, language: str = "en") -> dict:
        seed = sum(ord(c) for c in location_name)
        tempC = 28.0 + (seed % 5)
        humidity = 70 + (seed % 18)
        wind_speed = 12.0 + (seed % 6)
        rain_mm = 2.0 if humidity > 75 else 0.0

        forecast_list = []
        for i in range(5):
            d = (datetime.utcnow() + timedelta(days=i)).strftime("%Y-%m-%d")
            h = min(95, max(55, humidity + i * 2 - 1))
            forecast_list.append({
                "date": d,
                "time": f"{d} 12:00:00",
                "temp": tempC + i * 0.5,
                "temp_max": tempC + 3,
                "temp_min": tempC - 4,
                "humidity": h,
                "condition": "Partly Cloudy",
                "rainfall_mm": i * 1.5,
                "disease_risk": "High" if h > 75 else "Medium",
                "risk_reason": "High humidity favors fungal spore germination" if h > 75 else "Favorable conditions"
            })

        return WeatherService._format_weather_response(
            location=location_name,
            state="Maharashtra",
            tempC=tempC,
            condition="Partly Cloudy & Humid",
            humidity=humidity,
            wind_speed=wind_speed,
            rain_mm=rain_mm,
            forecast_list=forecast_list,
            language=language
        )

@router.get("")
@router.get("/")
def get_weather(
    request: Request,
    lat: Optional[float] = Query(None, description="Latitude GPS coordinate"),
    lon: Optional[float] = Query(None, description="Longitude GPS coordinate"),
    city: Optional[str] = Query(None, description="City name"),
    language: Optional[str] = Query(None, description="Language code")
):
    """Get live weather forecast data by GPS coordinates or city"""
    lang = _resolve_language(request, language)
    return WeatherService.fetch_weather(lat=lat, lon=lon, city=city or "getting location", language=lang)

@router.get("/forecast")
def get_weather_forecast(
    request: Request,
    lat: Optional[float] = Query(None, description="Latitude GPS coordinate"),
    lon: Optional[float] = Query(None, description="Longitude GPS coordinate"),
    city: Optional[str] = Query(None, description="City name"),
    language: Optional[str] = Query(None, description="Language code")
):
    """Get 5-day live weather forecast by GPS coordinates or city"""
    lang = _resolve_language(request, language)
    return WeatherService.fetch_weather(lat=lat, lon=lon, city=city or "getting location", language=lang)

@router.get("/current")
def get_current_weather(
    request: Request,
    lat: Optional[float] = Query(None, description="Latitude GPS coordinate"),
    lon: Optional[float] = Query(None, description="Longitude GPS coordinate"),
    city: Optional[str] = Query(None, description="City name"),
    language: Optional[str] = Query(None, description="Language code")
):
    """Get current weather conditions by GPS coordinates or city"""
    lang = _resolve_language(request, language)
    return WeatherService.fetch_weather(lat=lat, lon=lon, city=city or "getting location", language=lang)



