"""
Unit Tests for Layer 1 — Urgency Scoring Service
"""
import pytest
from datetime import datetime, timezone, timedelta
from app.services.urgency_service import (
    calculate_urgency_score,
    parse_timestamp_to_days_ago,
    extract_hours_until_rain,
    UrgencyResult,
    UrgencyBreakdown
)


def test_low_urgency_healthy():
    """Test 1: Healthy plant produces score 1 / low / green with 0 breakdown."""
    res = calculate_urgency_score(
        disease_name="Apple___healthy",
        confidence=98.0,
        progression_risk={"risk": "No Risk"}
    )
    assert res.urgency_score == 1
    assert res.urgency_level == "low"
    assert res.color == "green"
    assert res.breakdown.progression_score == 0.0
    assert res.breakdown.weather_score == 0.0
    assert res.breakdown.sensor_score == 0.0
    assert res.breakdown.delay_score == 0.0


def test_low_urgency_mild_disease():
    """Test 2: Low progression risk + dry/normal weather -> score 1-3."""
    res = calculate_urgency_score(
        disease_name="Tomato___Early_blight",
        confidence=65.0,
        progression_risk={"risk": "Low Risk"},
        weather_data={"humidity": 45, "rain_mm": 0, "rainfallChance": 10},
        sensor_data={"humidity": 45}
    )
    assert 1 <= res.urgency_score <= 3
    assert res.urgency_level == "low"
    assert res.color == "green"


def test_moderate_urgency():
    """Test 3: Medium progression risk + moderate humidity -> score 4-6."""
    res = calculate_urgency_score(
        disease_name="Potato___Late_blight",
        confidence=80.0,
        progression_risk={"risk": "Medium Risk"},
        weather_data={"humidity": 65, "rainfallChance": 40},
        sensor_data={"humidity": 68}
    )
    assert 4 <= res.urgency_score <= 6
    assert res.urgency_level == "moderate"
    assert res.color == "yellow"


def test_high_urgency():
    """Test 4: High progression risk + high humidity -> score 7-8."""
    res = calculate_urgency_score(
        disease_name="Tomato___Early_blight",
        confidence=92.0,
        progression_risk={"risk": "High Risk"},
        weather_data={"humidity": 80, "rainfallChance": 60},
        sensor_data={"humidity": 82}
    )
    assert 7 <= res.urgency_score <= 8
    assert res.urgency_level == "high"
    assert res.color == "orange"


def test_critical_urgency_with_rain():
    """Test 5: Severe Outbreak Risk + Imminent Rain (4h) + Extreme Humidity (88%) -> score 9-10."""
    now = datetime.now(timezone.utc)
    rain_time = (now + timedelta(hours=4)).isoformat()
    res = calculate_urgency_score(
        disease_name="Corn___Common_rust",
        confidence=95.0,
        progression_risk={"risk": "Severe Outbreak Risk"},
        weather_data={
            "humidity": 88,
            "forecast_list": [
                {"time": rain_time, "rainfall_mm": 5.0, "condition": "Heavy Rain"}
            ]
        },
        sensor_data={"humidity": 90},
        days_since_detection=2
    )
    assert 9 <= res.urgency_score <= 10
    assert res.urgency_level == "critical"
    assert res.color == "red"
    assert res.hours_until_rain is not None
    assert res.hours_until_rain <= 6.0


def test_missing_weather():
    """Test 6: Missing weather should still produce a valid 1-10 score without crashing."""
    res = calculate_urgency_score(
        disease_name="Tomato___Early_blight",
        confidence=90.0,
        progression_risk={"risk": "High Risk"},
        weather_data=None,
        sensor_data={"humidity": 70}
    )
    assert 1 <= res.urgency_score <= 10
    assert res.breakdown.weather_score == 0.0


def test_missing_sensor():
    """Test 7: Disconnected/missing sensor should not crash or overpenalize."""
    res = calculate_urgency_score(
        disease_name="Tomato___Early_blight",
        confidence=90.0,
        progression_risk={"risk": "Medium Risk"},
        weather_data={"humidity": 50},
        sensor_data=None
    )
    assert 1 <= res.urgency_score <= 10
    assert res.breakdown.sensor_score == 0.0


def test_missing_detection_timestamp():
    """Test 8: Missing history timestamp defaults delay factor to 0 without crashing."""
    res = calculate_urgency_score(
        disease_name="Tomato___Early_blight",
        confidence=90.0,
        progression_risk={"risk": "Medium Risk"},
        detection_timestamp=None,
        days_since_detection=None
    )
    assert 1 <= res.urgency_score <= 10
    assert res.breakdown.delay_score == 0.0


def test_rain_proximity_increases_score():
    """Test 9: Rain in 3h produces higher weather contribution than rain in 48h."""
    now = datetime.now(timezone.utc)
    res_near = calculate_urgency_score(
        disease_name="Tomato___Early_blight",
        progression_risk={"risk": "Medium Risk"},
        weather_data={
            "forecast_list": [{"time": (now + timedelta(hours=3)).isoformat(), "rainfall_mm": 2.0, "condition": "Rain"}]
        }
    )
    res_far = calculate_urgency_score(
        disease_name="Tomato___Early_blight",
        progression_risk={"risk": "Medium Risk"},
        weather_data={
            "forecast_list": [{"time": (now + timedelta(hours=48)).isoformat(), "rainfall_mm": 2.0, "condition": "Rain"}]
        }
    )
    assert res_near.breakdown.weather_score > res_far.breakdown.weather_score


def test_increasing_humidity_increases_score():
    """Test 10: 90% humidity produces higher sensor contribution than 50% humidity."""
    res_high_hum = calculate_urgency_score(
        disease_name="Tomato___Early_blight",
        progression_risk={"risk": "Medium Risk"},
        sensor_data={"humidity": 90}
    )
    res_low_hum = calculate_urgency_score(
        disease_name="Tomato___Early_blight",
        progression_risk={"risk": "Medium Risk"},
        sensor_data={"humidity": 50}
    )
    assert res_high_hum.breakdown.sensor_score > res_low_hum.breakdown.sensor_score


def test_increasing_delay_increases_score():
    """Test 11: 4 days delay produces higher delay score than same-day detection."""
    res_delayed = calculate_urgency_score(
        disease_name="Tomato___Early_blight",
        progression_risk={"risk": "Medium Risk"},
        days_since_detection=4
    )
    res_fresh = calculate_urgency_score(
        disease_name="Tomato___Early_blight",
        progression_risk={"risk": "Medium Risk"},
        days_since_detection=0
    )
    assert res_delayed.breakdown.delay_score > res_fresh.breakdown.delay_score


def test_multilingual_instruction():
    """Test 12: Instructions and reasons are localized for Tamil and Hindi."""
    res_ta = calculate_urgency_score(
        disease_name="Tomato___Early_blight",
        progression_risk={"risk": "Severe Outbreak Risk"},
        language="ta"
    )
    assert any(ord(c) >= 0x0B80 and ord(c) <= 0x0BFF for c in res_ta.instruction)

    res_hi = calculate_urgency_score(
        disease_name="Tomato___Early_blight",
        progression_risk={"risk": "Severe Outbreak Risk"},
        language="hi"
    )
    assert any(ord(c) >= 0x0900 and ord(c) <= 0x097F for c in res_hi.instruction)
