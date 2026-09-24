"""
Urgency Scoring Service for AgriGuard
Deterministic, explainable synthesis of:
1. Disease Progression (Gemini AI / Fallback)
2. Weather Telemetry & Incoming Rain ETA
3. IoT Sensor Microclimate (Canopy Humidity / Soil Moisture)
4. Days Since Detection (Untreated Delay Factor)

Produces a standardized 1-10 Urgency Score, Level, Semantic Color,
Primary Farmer Instruction, Contextual Reason, and Factor Breakdown.
"""

from datetime import datetime, timezone, timedelta
from typing import Optional, Dict, Any, Union
from pydantic import BaseModel
import logging
import re

logger = logging.getLogger(__name__)


class UrgencyBreakdown(BaseModel):
    progression_score: float  # 0.0 - 4.0
    weather_score: float      # 0.0 - 2.5
    sensor_score: float       # 0.0 - 2.0
    delay_score: float        # 0.0 - 1.5


class UrgencyResult(BaseModel):
    urgency_score: int                           # 1 - 10
    urgency_level: str                           # "low" | "moderate" | "high" | "critical"
    color: str                                   # "green" | "yellow" | "orange" | "red"
    instruction: str                             # Primary farmer action directive
    reason: str                                  # Explainable contextual rationale
    days_since_detection: Optional[int] = None   # Days elapsed since first/prior detection
    hours_until_rain: Optional[float] = None     # Hours until forecasted rain (if available)
    breakdown: Optional[UrgencyBreakdown] = None # Component contributions


# ─────────────────────────────────────────────────────────────────────────────
# Localized Instruction & Reason Templates (Supports 25 Languages)
# ─────────────────────────────────────────────────────────────────────────────

URGENCY_INSTRUCTIONS_25 = {
    "en": {
        "critical_rain": "Take action within the next few hours.",
        "critical": "Take immediate action.",
        "high": "Take action within 24 hours.",
        "moderate": "Take action soon and prepare treatment.",
        "low": "Monitor conditions closely.",
        "healthy": "No action required. Plant foliage is healthy."
    },
    "hi": {
        "critical_rain": "अगले कुछ घंटों के भीतर तुरंत कार्रवाई करें।",
        "critical": "तत्काल उपचार शुरू करें।",
        "high": "अगले 24 घंटों के भीतर कार्रवाई करें।",
        "moderate": "जल्द ही उपचार की तैयारी करें और छिड़काव करें।",
        "low": "फसल की स्थिति पर करीबी नज़र रखें।",
        "healthy": "किसी कार्रवाई की आवश्यकता नहीं है। पौधा स्वस्थ है।"
    },
    "ta": {
        "critical_rain": "அடுத்த சில மணிநேரங்களுக்குள் உடனடியாக நடவடிக்கை எடுக்கவும்.",
        "critical": "உடனடி சிகிச்சை நடவடிக்கைகளைத் தொடங்கவும்.",
        "high": "அடுத்த 24 மணிநேரத்திற்குள் சிகிச்சை அளிக்கவும்.",
        "moderate": "விரைவில் மருந்து தெளிக்கத் தயாராகுங்கள்.",
        "low": "பயிரின் நிலையைத் தொடர்ந்து கண்காணிக்கவும்.",
        "healthy": "எந்த நடவடிக்கையும் தேவையில்லை. இலைகள் ஆரோக்கியமாக உள்ளன."
    },
    "te": {
        "critical_rain": "రాబోయే కొన్ని గంటల్లో వెంటనే చర్య తీసుకోండి.",
        "critical": "వెంటనే నివారణ చర్యలు ప్రారంభించండి.",
        "high": "రాబోయే 24 గంటల్లో చర్య తీసుకోండి.",
        "moderate": "త్వరలోనే చికిత్సకు సిద్ధం కండి.",
        "low": "పరిస్థితులను నిశితంగా పరిశీలించండి.",
        "healthy": "ఎటువంటి చర్య అవసరం లేదు. మొక్క ఆరోగ్యంగా ఉంది."
    },
    "ml": {
        "critical_rain": "അടുത്ത ഏതാനും മണിക്കൂറുകൾക്കുള്ളിൽ നടപടിയെടുക്കുക.",
        "critical": "ഉടൻ തന്നെ ചികിത്സാ നടപടികൾ ആരംഭിക്കുക.",
        "high": "24 മണിക്കൂറിനുള്ളിൽ നടപടിയെടുക്കുക.",
        "moderate": "ഉടൻ തന്നെ മരുന്ന് തളിക്കാൻ തയ്യാറെടുക്കുക.",
        "low": "വിളകളുടെ അവസ്ഥ സൂക്ഷ്മമായി നിരീക്ഷിക്കുക.",
        "healthy": "നടപടിയുടെ ആവശ്യമില്ല. ചെടി ആരോഗ്യകരമാണ്."
    },
    "kn": {
        "critical_rain": "ಮುಂದಿನ ಕೆಲವೇ ಗಂಟೆಗಳಲ್ಲಿ ತಕ್ಷಣ ಕ್ರಮ ಕೈಗೊಳ್ಳಿ.",
        "critical": "ತಕ್ಷಣವೇ ಚಿಕಿತ್ಸಾ ಕ್ರಮಗಳನ್ನು ಕೈಗೊಳ್ಳಿ.",
        "high": "ಮುಂದಿನ 24 ಗಂಟೆಗಳಲ್ಲಿ ಕ್ರಮ ತೆಗೆದುಕೊಳ್ಳಿ.",
        "moderate": "ಶೀಘ್ರದಲ್ಲೇ ಚಿಕಿತ್ಸೆಗೆ ಸಿದ್ಧರಾಗಿ.",
        "low": "ಬೆಳೆಯ ಪರಿಸ್ಥಿತಿಯನ್ನು ಸೂಕ್ಷ್ಮವಾಗಿ ಗಮನಿಸಿ.",
        "healthy": "ಯಾವುದೇ ಕ್ರಮ ಅಗತ್ಯವಿಲ್ಲ. ಸಸ್ಯವು ಆರೋಗ್ಯಕರವಾಗಿದೆ."
    },
    "mr": {
        "critical_rain": "पुढील काही तासांत त्वरित कारवाई करा.",
        "critical": "तातडीने उपचारात्मक फवारणी सुरू करा.",
        "high": "पुढील २४ तासांत उपाययोजना करा.",
        "moderate": "लवकरच उपचारांची तयारी करा.",
        "low": "पिकांच्या स्थितीवर बारकाईने लक्ष ठेवा.",
        "healthy": "कोणत्याही कारवाईची गरज नाही. पीक निरोगी आहे."
    },
    "bn": {
        "critical_rain": "পরবর্তী কয়েক ঘণ্টার মধ্যে অবিলম্বে ব্যবস্থা নিন।",
        "critical": "অবিলম্বে প্রতিকারমূলক ব্যবস্থা গ্রহণ করুন।",
        "high": "পরবর্তী ২৪ ঘণ্টার মধ্যে ব্যবস্থা নিন।",
        "moderate": "শীঘ্রই চিকিৎসার প্রস্তুতি নিন।",
        "low": "পরিস্থিতি সতর্কতার সাথে পর্যবেক্ষণ করুন।",
        "healthy": "কোনো ব্যবস্থার প্রয়োজন নেই। পাতা স্বাস্থ্যকর।"
    },
    "gu": {
        "critical_rain": "આગામી થોડા કલાકોમાં તાત્કાલિક પગલાં લો.",
        "critical": "ત્વરિત સારવાર શરૂ કરો.",
        "high": "આગામી ૨૪ કલાકમાં પગલાં લો.",
        "moderate": "ટૂંક સમયમાં સારવારની તૈયારી કરો.",
        "low": "પાકની સ્થિતિનું નિરીક્ષણ કરો.",
        "healthy": "કોઈ પગલાં લેવાની જરૂર નથી. પાંદડા સ્વસ્થ છે."
    },
    "pa": {
        "critical_rain": "ਅਗਲੇ ਕੁਝ ਘੰਟਿਆਂ ਵਿੱਚ ਤੁਰੰਤ ਕਾਰਵਾਈ ਕਰੋ।",
        "critical": "ਤੁਰੰਤ ਇਲਾਜ ਸ਼ੁਰੂ ਕਰੋ।",
        "high": "ਅਗਲੇ 24 ਘੰਟਿਆਂ ਵਿੱਚ ਕਾਰਵਾਈ ਕਰੋ।",
        "moderate": "ਜਲਦੀ ਹੀ ਇਲਾਜ ਦੀ ਤਿਆਰੀ ਕਰੋ।",
        "low": "ਫਸਲ ਦੀ ਸਥਿਤੀ 'ਤੇ ਨਜ਼ਰ ਰੱਖੋ।",
        "healthy": "ਕੋਈ ਕਾਰਵਾਈ ਕਰਨ ਦੀ ਲੋੜ ਨਹੀਂ। ਪੌਦਾ ਤੰਦਰੁਸਤ ਹੈ।"
    }
}


def parse_timestamp_to_days_ago(ts: Optional[Union[str, datetime]]) -> Optional[int]:
    """
    Safely calculates integer days elapsed since a detection timestamp.
    Handles ISO strings, timezone offsets, missing values, and future timestamps.
    """
    if not ts:
        return None

    try:
        now = datetime.now(timezone.utc)

        if isinstance(ts, datetime):
            dt = ts if ts.tzinfo else ts.replace(tzinfo=timezone.utc)
        elif isinstance(ts, str):
            clean_ts = ts.strip()
            if not clean_ts:
                return None
            # Handle standard ISO formats with trailing Z or timezone offsets
            clean_ts = clean_ts.replace("Z", "+00:00")
            # Truncate fractional seconds beyond microseconds if present
            clean_ts = re.sub(r'(\.\d{6})\d+', r'\1', clean_ts)
            dt = datetime.fromisoformat(clean_ts)
            if not dt.tzinfo:
                dt = dt.replace(tzinfo=timezone.utc)
        else:
            return None

        delta = now - dt
        days = delta.total_seconds() / 86400.0

        # Protect against future clock-skew
        if days < 0:
            return 0

        return int(max(0, round(days)))
    except Exception as e:
        logger.debug(f"Could not parse detection timestamp '{ts}': {e}")
        return None


def extract_hours_until_rain(weather_data: Optional[Dict[str, Any]]) -> Optional[float]:
    """
    Extracts the earliest hours until forecasted precipitation from weather telemetry.
    Returns hours (e.g. 3.0, 6.0, 18.0) or None if no reliable rain event is scheduled.
    """
    if not weather_data or not isinstance(weather_data, dict):
        return None

    now = datetime.now(timezone.utc)

    # 1. Check current conditions
    rain_mm = weather_data.get("rain_mm", 0)
    cond = str(weather_data.get("condition", "")).lower()
    if rain_mm and float(rain_mm) > 0.2:
        return 0.0
    if any(k in cond for k in ["rain", "storm", "drizzle", "shower", "thunder"]):
        return 0.0

    # 2. Check 3-hour / 5-day forecast list
    forecast_items = weather_data.get("forecast_list") or weather_data.get("forecast") or []
    if isinstance(forecast_items, list):
        for idx, item in enumerate(forecast_items):
            if not isinstance(item, dict):
                continue

            item_rain = float(item.get("rainfall_mm") or item.get("rain_mm") or item.get("rain", 0) or 0)
            item_cond = str(item.get("condition", "")).lower()
            is_rainy = item_rain >= 0.5 or any(k in item_cond for k in ["rain", "storm", "drizzle", "shower"])

            if is_rainy:
                # Try parsing explicit forecast timestamp
                time_str = item.get("time") or item.get("dt_txt") or item.get("date")
                if time_str:
                    try:
                        time_clean = time_str.replace("Z", "+00:00")
                        if " " in time_clean and "T" not in time_clean:
                            time_clean = time_clean.replace(" ", "T")
                        dt_forecast = datetime.fromisoformat(time_clean)
                        if not dt_forecast.tzinfo:
                            dt_forecast = dt_forecast.replace(tzinfo=timezone.utc)
                        hours = (dt_forecast - now).total_seconds() / 3600.0
                        if hours >= 0:
                            return round(hours, 1)
                    except Exception:
                        pass

                # Fallback: estimate from 3h / daily index
                return float(max(1, (idx + 1) * 3))

    return None


def calculate_urgency_score(
    disease_name: str,
    confidence: float = 90.0,
    progression_risk: Optional[Dict[str, Any]] = None,
    weather_data: Optional[Dict[str, Any]] = None,
    sensor_data: Optional[Dict[str, Any]] = None,
    detection_timestamp: Optional[Union[str, datetime]] = None,
    days_since_detection: Optional[int] = None,
    language: str = "en"
) -> UrgencyResult:
    """
    Synthesizes disease progression, weather, IoT telemetry, and detection history
    into a deterministic 1-10 Urgency Score with explainable breakdown.

    Scoring Weights:
    - Base Disease Presence: 1.0 point
    - Disease Progression:   0.0 - 4.0 points (Strongest factor)
    - Incoming Rain/Weather: 0.0 - 2.5 points (Rain acceleration factor)
    - IoT Sensor Humidity:   0.0 - 2.0 points (Microclimate humidity factor)
    - Detection Age/Delay:   0.0 - 1.5 points (Untreated delay factor)
    Total Potential Raw:     1.0 - 11.0 -> Clamped strictly to 1 - 10.
    """
    lang = (language or "en").lower().strip()
    is_healthy = "healthy" in disease_name.lower() or (
        progression_risk and str(progression_risk.get("risk", "")).lower() == "no risk"
    )

    # ─────────────────────────────────────────────────────────────────────────
    # CASE 1: HEALTHY PLANT (Score 1 / Low / Green)
    # ─────────────────────────────────────────────────────────────────────────
    if is_healthy:
        inst_dict = URGENCY_INSTRUCTIONS_25.get(lang, URGENCY_INSTRUCTIONS_25["en"])
        instruction = inst_dict.get("healthy", URGENCY_INSTRUCTIONS_25["en"]["healthy"])
        return UrgencyResult(
            urgency_score=1,
            urgency_level="low",
            color="green",
            instruction=instruction,
            reason="Optimal plant health with no active pathogen pressure.",
            days_since_detection=0,
            hours_until_rain=None,
            breakdown=UrgencyBreakdown(
                progression_score=0.0,
                weather_score=0.0,
                sensor_score=0.0,
                delay_score=0.0
            )
        )

    # ─────────────────────────────────────────────────────────────────────────
    # FACTOR 1: Disease Progression Score (0.0 - 4.0)
    # ─────────────────────────────────────────────────────────────────────────
    progression_score = 0.0
    risk_str = ""

    if progression_risk and isinstance(progression_risk, dict):
        risk_str = str(progression_risk.get("risk", "")).lower()
        if "severe" in risk_str:
            progression_score = 4.0
        elif "high" in risk_str:
            progression_score = 3.0
        elif "medium" in risk_str or "moderate" in risk_str:
            progression_score = 2.0
        elif "low" in risk_str:
            progression_score = 1.0
        elif "no risk" in risk_str:
            progression_score = 0.0
        else:
            progression_score = 2.0
    else:
        # Fallback based on model confidence
        if confidence >= 85.0:
            progression_score = 2.5
        elif confidence >= 70.0:
            progression_score = 2.0
        else:
            progression_score = 1.5

    # ─────────────────────────────────────────────────────────────────────────
    # FACTOR 2: Weather & Incoming Rain Score (0.0 - 2.5)
    # ─────────────────────────────────────────────────────────────────────────
    weather_score = 0.0
    hours_until_rain = extract_hours_until_rain(weather_data)

    if hours_until_rain is not None:
        if hours_until_rain <= 6.0:
            weather_score = 2.5  # Imminent rain: urgent protective spray needed before rain
        elif hours_until_rain <= 18.0:
            weather_score = 2.0  # Approaching within 18h
        elif hours_until_rain <= 36.0:
            weather_score = 1.5  # Approaching in 24-36h
        elif hours_until_rain <= 72.0:
            weather_score = 0.5
    elif weather_data and isinstance(weather_data, dict):
        # Fallback to general rainfall probability if no hourly ETA
        rain_prob = weather_data.get("rainfallChance") or weather_data.get("rain_prob") or 0
        try:
            prob_val = float(rain_prob)
            if prob_val >= 75.0:
                weather_score = 1.8
            elif prob_val >= 55.0:
                weather_score = 1.2
            elif prob_val >= 35.0:
                weather_score = 0.6
        except (ValueError, TypeError):
            pass

    # ─────────────────────────────────────────────────────────────────────────
    # FACTOR 3: IoT Sensor & Canopy Humidity Score (0.0 - 2.0)
    # ─────────────────────────────────────────────────────────────────────────
    sensor_score = 0.0
    measured_humidity = None

    if sensor_data and isinstance(sensor_data, dict):
        measured_humidity = sensor_data.get("humidity")

    if measured_humidity is None and weather_data and isinstance(weather_data, dict):
        measured_humidity = weather_data.get("humidity")

    if measured_humidity is not None:
        try:
            hum_val = float(measured_humidity)
            if hum_val >= 85.0:
                sensor_score = 2.0  # Extreme humidity (>85% RH triggers rapid sporulation)
            elif hum_val >= 75.0:
                sensor_score = 1.5  # High humidity (>75% RH supports germination)
            elif hum_val >= 60.0:
                sensor_score = 0.8  # Moderate humidity
            else:
                sensor_score = 0.0
        except (ValueError, TypeError):
            sensor_score = 0.0

    # ─────────────────────────────────────────────────────────────────────────
    # FACTOR 4: Days Since Detection / Delay Score (0.0 - 1.5)
    # ─────────────────────────────────────────────────────────────────────────
    delay_score = 0.0
    days_elapsed = days_since_detection

    if days_elapsed is None and detection_timestamp:
        days_elapsed = parse_timestamp_to_days_ago(detection_timestamp)

    if days_elapsed is not None and days_elapsed > 0:
        if days_elapsed >= 4:
            delay_score = 1.5  # 4+ days delay
        elif days_elapsed >= 2:
            delay_score = 1.0  # 2-3 days delay
        elif days_elapsed >= 1:
            delay_score = 0.5  # 1 day delay

    # ─────────────────────────────────────────────────────────────────────────
    # FINAL SYNTHESIS & CLAMPING (1 - 10)
    # ─────────────────────────────────────────────────────────────────────────
    base_score = 1.0
    raw_total = base_score + progression_score + weather_score + sensor_score + delay_score
    final_score = int(max(1, min(10, round(raw_total))))

    # Level & Color Classification
    if final_score >= 9:
        urgency_level = "critical"
        color = "red"
    elif final_score >= 7:
        urgency_level = "high"
        color = "orange"
    elif final_score >= 4:
        urgency_level = "moderate"
        color = "yellow"
    else:
        urgency_level = "low"
        color = "green"

    # Contextual Farmer Instruction & Reason Generation
    inst_dict = URGENCY_INSTRUCTIONS_25.get(lang, URGENCY_INSTRUCTIONS_25["en"])

    if hours_until_rain is not None and hours_until_rain <= 12.0 and final_score >= 7:
        instruction = inst_dict.get("critical_rain", URGENCY_INSTRUCTIONS_25["en"]["critical_rain"])
        hum_text = f" and humidity is {int(measured_humidity)}%" if measured_humidity else ""
        reason = f"Rain is forecast in approximately {int(hours_until_rain)} hours{hum_text}. Apply treatment before rainfall."
    elif urgency_level == "critical":
        instruction = inst_dict.get("critical", URGENCY_INSTRUCTIONS_25["en"]["critical"])
        reason = "Severe disease progression risk with elevated environmental vulnerability."
    elif urgency_level == "high":
        instruction = inst_dict.get("high", URGENCY_INSTRUCTIONS_25["en"]["high"])
        hum_text = f"Elevated canopy humidity ({int(measured_humidity)}%)" if measured_humidity and float(measured_humidity) >= 75 else "Active symptoms"
        reason = f"{hum_text} and disease progression require treatment within 24 hours."
    elif urgency_level == "moderate":
        instruction = inst_dict.get("moderate", URGENCY_INSTRUCTIONS_25["en"]["moderate"])
        reason = "Pathogen symptoms detected. Prepare treatment protocol and monitor field moisture."
    else:
        instruction = inst_dict.get("low", URGENCY_INSTRUCTIONS_25["en"]["low"])
        reason = "Low spread velocity under current microclimate conditions."

    if days_elapsed and days_elapsed >= 2:
        reason += f" ({days_elapsed} days elapsed since first detection)."

    return UrgencyResult(
        urgency_score=final_score,
        urgency_level=urgency_level,
        color=color,
        instruction=instruction,
        reason=reason,
        days_since_detection=days_elapsed,
        hours_until_rain=hours_until_rain,
        breakdown=UrgencyBreakdown(
            progression_score=round(progression_score, 2),
            weather_score=round(weather_score, 2),
            sensor_score=round(sensor_score, 2),
            delay_score=round(delay_score, 2)
        )
    )
