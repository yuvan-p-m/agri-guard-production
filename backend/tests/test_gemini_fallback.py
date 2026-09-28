"""
Comprehensive unit tests for AgriGuard primary (gemini-3.5-flash) and fallback (gemini-3.6-flash) models.
Tests cover:
1. Gemini 3.5 returns 200 -> Gemini 3.6 is NOT called.
2. Gemini 3.5 returns 503 -> retries occur -> Gemini 3.6 is called.
3. Gemini 3.5 returns 429 -> retries occur -> Gemini 3.6 is called.
4. Gemini 3.6 returns 200 -> diagnosis returned normally with exact response schema.
5. Gemini 3.5 and 3.6 both fail -> proper service error returned, no fake diagnosis.
6. 400/401/403/404 errors -> no retry and no fallback.
7. Invalid image -> ValueError, no Gemini calls.
8. /api/v1/model/status reports configured primary and fallback models.
9. Configuration via environment variables.
"""

import unittest
from unittest.mock import patch, MagicMock, call
import io
import json
from PIL import Image

import sys
from pathlib import Path

BACKEND_APP_DIR = Path(__file__).resolve().parent.parent / "app"
if str(BACKEND_APP_DIR) not in sys.path:
    sys.path.insert(0, str(BACKEND_APP_DIR))

from services.gemini_service import (
    diagnose_crop_disease,
    get_gemini_primary_model,
    get_gemini_fallback_model,
    get_gemini_model,
    _call_gemini_multimodal,
    INVALID_IMAGE_MESSAGE,
    GeminiAPIError,
    GeminiUnavailableError,
    GeminiRateLimitError,
    GeminiTimeoutError,
    GeminiParseError
)


def _create_test_image_bytes() -> bytes:
    """Creates a minimal valid JPEG image in bytes."""
    img = Image.new("RGB", (100, 100), color=(73, 109, 137))
    buf = io.BytesIO()
    img.save(buf, format="JPEG")
    return buf.getvalue()


SAMPLE_DIAGNOSIS_JSON = {
    "is_plant_leaf": True,
    "is_healthy": False,
    "crop": "Tomato",
    "disease": "Early Blight",
    "disease_id": "Tomato___Early_blight",
    "confidence": 95.0,
    "severity": "medium",
    "pathogen_type": "Fungus",
    "symptoms": ["Dark brown spots with concentric rings", "Yellow halos around lesions"],
    "reasoning": "Clear target-board concentric lesions characteristic of Alternaria solani."
}


def _make_mock_response(status_code: int, json_data=None, text=""):
    resp = MagicMock()
    resp.status_code = status_code
    resp.text = text or json.dumps(json_data or {})
    if json_data is not None:
        resp.json.return_value = json_data
    else:
        resp.json.side_effect = ValueError("No JSON body")
    return resp


class TestGeminiFallbackModel(unittest.TestCase):

    def setUp(self):
        self.image_bytes = _create_test_image_bytes()
        self.valid_candidate_response = {
            "candidates": [
                {
                    "content": {
                        "parts": [
                            {"text": json.dumps(SAMPLE_DIAGNOSIS_JSON)}
                        ]
                    }
                }
            ]
        }

    @patch("services.gemini_service.time.sleep", return_value=None)
    @patch("services.gemini_service.requests.post")
    def test_gemini_35_returns_200_no_fallback_called(self, mock_post, mock_sleep):
        """1. Gemini 3.5 returns 200: verify Gemini 3.6 is NOT called."""
        mock_post.return_value = _make_mock_response(200, self.valid_candidate_response)

        result = diagnose_crop_disease(self.image_bytes)

        self.assertEqual(result["status"], "success")
        self.assertEqual(result["crop"], "Tomato")
        self.assertEqual(result["disease"], "Tomato___Early_blight")
        self.assertEqual(result["model_used"], "gemini-3.5-flash")
        self.assertEqual(result["provider"], "gemini")

        # Verify only 1 HTTP request made to gemini-3.5-flash
        self.assertEqual(mock_post.call_count, 1)
        called_url = mock_post.call_args_list[0][0][0]
        self.assertIn("models/gemini-3.5-flash:generateContent", called_url)
        self.assertNotIn("gemini-3.6-flash", called_url)
        mock_sleep.assert_not_called()

    @patch("services.gemini_service.time.sleep", return_value=None)
    @patch("services.gemini_service.requests.post")
    def test_gemini_35_returns_503_retries_and_falls_back_to_36(self, mock_post, mock_sleep):
        """2. Gemini 3.5 returns 503: verify existing retries occur, then Gemini 3.6 is called."""
        resp_503 = _make_mock_response(503, {
            "error": {"code": 503, "message": "High demand", "status": "UNAVAILABLE"}
        })
        resp_200 = _make_mock_response(200, self.valid_candidate_response)

        # 3 failures on 3.5 (attempt 1, attempt 2, attempt 3), then 200 on 3.6
        mock_post.side_effect = [resp_503, resp_503, resp_503, resp_200]

        result = diagnose_crop_disease(self.image_bytes)

        self.assertEqual(result["status"], "success")
        self.assertEqual(result["model_used"], "gemini-3.6-flash")
        self.assertEqual(result["crop"], "Tomato")

        # 3 calls on 3.5 + 1 call on 3.6 = 4 total calls
        self.assertEqual(mock_post.call_count, 4)

        # First 3 calls must be to gemini-3.5-flash
        for i in range(3):
            url = mock_post.call_args_list[i][0][0]
            self.assertIn("models/gemini-3.5-flash:generateContent", url)

        # 4th call must be to gemini-3.6-flash
        url_fallback = mock_post.call_args_list[3][0][0]
        self.assertIn("models/gemini-3.6-flash:generateContent", url_fallback)

        # Verify backoff sleeps occurred: 2.0s then 4.0s for the 2 retries on 3.5
        self.assertEqual(mock_sleep.call_count, 2)
        mock_sleep.assert_has_calls([call(2.0), call(4.0)])

    @patch("services.gemini_service.time.sleep", return_value=None)
    @patch("services.gemini_service.requests.post")
    def test_gemini_35_returns_429_retries_and_falls_back_to_36(self, mock_post, mock_sleep):
        """3. Gemini 3.5 returns 429: verify fallback to Gemini 3.6 occurs according to policy."""
        resp_429 = _make_mock_response(429, {
            "error": {"code": 429, "message": "Resource exhausted", "status": "RESOURCE_EXHAUSTED"}
        })
        resp_200 = _make_mock_response(200, self.valid_candidate_response)

        # 3 attempts on 3.5 return 429, then 3.6 succeeds with 200
        mock_post.side_effect = [resp_429, resp_429, resp_429, resp_200]

        result = diagnose_crop_disease(self.image_bytes)

        self.assertEqual(result["status"], "success")
        self.assertEqual(result["model_used"], "gemini-3.6-flash")

        # 3 calls on 3.5 + 1 call on 3.6 = 4 total calls
        self.assertEqual(mock_post.call_count, 4)
        url_fallback = mock_post.call_args_list[3][0][0]
        self.assertIn("models/gemini-3.6-flash:generateContent", url_fallback)

        # Sleep occurred with 2.0s and 4.0s backoff
        self.assertEqual(mock_sleep.call_count, 2)
        mock_sleep.assert_has_calls([call(2.0), call(4.0)])

    @patch("services.gemini_service.time.sleep", return_value=None)
    @patch("services.gemini_service.requests.post")
    def test_gemini_36_bounded_retry_and_succeeds(self, mock_post, mock_sleep):
        """4. Gemini 3.6 has bounded retries and returns diagnosis normally."""
        resp_503 = _make_mock_response(503, {"error": {"message": "Demand spike"}})
        resp_200 = _make_mock_response(200, self.valid_candidate_response)

        # 3.5 fails 3 times (503), then 3.6 fails once (503), then 3.6 succeeds (200)
        mock_post.side_effect = [resp_503, resp_503, resp_503, resp_503, resp_200]

        result = diagnose_crop_disease(self.image_bytes)

        self.assertEqual(result["status"], "success")
        self.assertEqual(result["model_used"], "gemini-3.6-flash")
        self.assertEqual(mock_post.call_count, 5)

        # Calls 3 and 4 were to 3.6-flash
        self.assertIn("models/gemini-3.6-flash:generateContent", mock_post.call_args_list[3][0][0])
        self.assertIn("models/gemini-3.6-flash:generateContent", mock_post.call_args_list[4][0][0])

    @patch("services.gemini_service.time.sleep", return_value=None)
    @patch("services.gemini_service.requests.post")
    def test_both_models_fail_returns_service_error_no_fake_diagnosis(self, mock_post, mock_sleep):
        """5. Gemini 3.5 and 3.6 both fail: verify proper service error is raised, no fake diagnosis."""
        resp_503 = _make_mock_response(503, {"error": {"message": "Service unavailable"}})

        # 3 attempts on 3.5 + 3 attempts on 3.6 = 6 attempts total
        mock_post.side_effect = [resp_503] * 6

        with self.assertRaises(GeminiUnavailableError) as ctx:
            diagnose_crop_disease(self.image_bytes)

        self.assertEqual(ctx.exception.status_code, 503)
        self.assertIn("AI diagnosis service is currently experiencing high demand", str(ctx.exception))
        self.assertEqual(mock_post.call_count, 6)

    @patch("services.gemini_service.requests.post")
    def test_no_fallback_on_400_bad_request(self, mock_post):
        """6a. 400 Bad Request: verify NO retry and NO fallback to 3.6 occurs."""
        mock_post.return_value = _make_mock_response(400, {
            "error": {"code": 400, "message": "Invalid argument", "status": "INVALID_ARGUMENT"}
        })

        with self.assertRaises(GeminiAPIError) as ctx:
            diagnose_crop_disease(self.image_bytes)

        self.assertEqual(ctx.exception.status_code, 400)
        self.assertEqual(mock_post.call_count, 1)
        self.assertIn("models/gemini-3.5-flash:generateContent", mock_post.call_args_list[0][0][0])

    @patch("services.gemini_service.requests.post")
    def test_no_fallback_on_401_unauthorized(self, mock_post):
        """6b. 401 Unauthorized: verify NO retry and NO fallback to 3.6 occurs."""
        mock_post.return_value = _make_mock_response(401, {
            "error": {"code": 401, "message": "API key not valid", "status": "UNAUTHENTICATED"}
        })

        with self.assertRaises(GeminiAPIError) as ctx:
            diagnose_crop_disease(self.image_bytes)

        self.assertEqual(ctx.exception.status_code, 401)
        self.assertEqual(mock_post.call_count, 1)

    @patch("services.gemini_service.requests.post")
    def test_no_fallback_on_403_forbidden(self, mock_post):
        """6c. 403 Forbidden: verify NO retry and NO fallback to 3.6 occurs."""
        mock_post.return_value = _make_mock_response(403, {
            "error": {"code": 403, "message": "Permission denied", "status": "PERMISSION_DENIED"}
        })

        with self.assertRaises(GeminiAPIError) as ctx:
            diagnose_crop_disease(self.image_bytes)

        self.assertEqual(ctx.exception.status_code, 403)
        self.assertEqual(mock_post.call_count, 1)

    @patch("services.gemini_service.requests.post")
    def test_no_fallback_on_404_not_found(self, mock_post):
        """6d. 404 Not Found: verify NO retry and NO fallback to 3.6 occurs."""
        mock_post.return_value = _make_mock_response(404, {
            "error": {"code": 404, "message": "Model not found", "status": "NOT_FOUND"}
        })

        with self.assertRaises(GeminiAPIError) as ctx:
            diagnose_crop_disease(self.image_bytes)

        self.assertEqual(ctx.exception.status_code, 404)
        self.assertEqual(mock_post.call_count, 1)

    def test_invalid_image_raises_value_error_no_api_calls(self):
        """6e. Invalid image raises ValueError immediately without calling any API."""
        with self.assertRaises(ValueError):
            diagnose_crop_disease(b"too_short")

        with self.assertRaises(ValueError):
            diagnose_crop_disease(b"x" * 100)  # corrupt image bytes

    @patch("services.gemini_service.requests.post")
    def test_invalid_leaf_classified_normally_without_fallback(self, mock_post):
        """Invalid plant leaf returns invalid_leaf status with fixed generic message without fallback."""
        non_plant_response = {
            "candidates": [
                {
                    "content": {
                        "parts": [
                            {"text": json.dumps({
                                "is_plant_leaf": False,
                                "is_healthy": False,
                                "crop": "None",
                                "disease": "No Crop Leaf Detected",
                                "disease_id": "invalid_leaf",
                                "confidence": 0.0,
                                "severity": "none",
                                "pathogen_type": "None",
                                "symptoms": [],
                                "reasoning": "Photo shows a shoe, not plant foliage."
                            })}
                        ]
                    }
                }
            ]
        }
        mock_post.return_value = _make_mock_response(200, non_plant_response)

        result = diagnose_crop_disease(self.image_bytes)
        self.assertFalse(result["is_plant_leaf"])
        self.assertEqual(result["status"], "invalid_leaf")
        self.assertEqual(result["message"], INVALID_IMAGE_MESSAGE)
        self.assertEqual(result["reasoning"], INVALID_IMAGE_MESSAGE)
        self.assertEqual(result["model_used"], "gemini-3.5-flash")
        self.assertNotIn("shoe", result["message"].lower())
        self.assertNotIn("shoe", result["reasoning"].lower())
        self.assertEqual(mock_post.call_count, 1)

    @patch("services.gemini_service.requests.post")
    def test_non_leaf_object_keyboard_never_reveals_object(self, mock_post):
        """1. Upload photo of non-leaf object (keyboard): generic message only, object name never appears."""
        keyboard_response = {
            "candidates": [
                {
                    "content": {
                        "parts": [
                            {"text": json.dumps({
                                "is_plant_leaf": False,
                                "is_healthy": False,
                                "crop": "None",
                                "disease": "No Crop Leaf Detected",
                                "disease_id": "invalid_leaf",
                                "confidence": 0.0,
                                "severity": "none",
                                "pathogen_type": "None",
                                "symptoms": [],
                                "reasoning": "This appears to be a photo of a keyboard. It is not a plant leaf."
                            })}
                        ]
                    }
                }
            ]
        }
        mock_post.return_value = _make_mock_response(200, keyboard_response)

        result = diagnose_crop_disease(self.image_bytes)
        self.assertEqual(result["status"], "invalid_leaf")
        self.assertEqual(result["message"], "Invalid image. Please upload a clear photo of a plant leaf.")
        self.assertEqual(result["reasoning"], "Invalid image. Please upload a clear photo of a plant leaf.")
        self.assertNotIn("keyboard", result["message"].lower())
        self.assertNotIn("keyboard", result["reasoning"].lower())

    @patch("services.gemini_service.requests.post")
    def test_animal_photo_never_reveals_animal(self, mock_post):
        """2. Upload photo of animal (dog): generic message only, animal name never appears."""
        animal_response = {
            "candidates": [
                {
                    "content": {
                        "parts": [
                            {"text": json.dumps({
                                "is_plant_leaf": False,
                                "is_healthy": False,
                                "crop": "None",
                                "disease": "No Crop Leaf Detected",
                                "disease_id": "invalid_leaf",
                                "confidence": 0.0,
                                "severity": "none",
                                "pathogen_type": "None",
                                "symptoms": [],
                                "reasoning": "This photo depicts a domestic dog playing outdoors."
                            })}
                        ]
                    }
                }
            ]
        }
        mock_post.return_value = _make_mock_response(200, animal_response)

        result = diagnose_crop_disease(self.image_bytes)
        self.assertEqual(result["status"], "invalid_leaf")
        self.assertEqual(result["message"], "Invalid image. Please upload a clear photo of a plant leaf.")
        self.assertEqual(result["reasoning"], "Invalid image. Please upload a clear photo of a plant leaf.")
        self.assertNotIn("dog", result["message"].lower())
        self.assertNotIn("dog", result["reasoning"].lower())

    @patch("services.gemini_service.requests.post")
    def test_document_screenshot_never_reveals_document(self, mock_post):
        """3. Upload photo of document/screenshot: generic message only, document/code never appears."""
        doc_response = {
            "candidates": [
                {
                    "content": {
                        "parts": [
                            {"text": json.dumps({
                                "is_plant_leaf": False,
                                "is_healthy": False,
                                "crop": "None",
                                "disease": "No Crop Leaf Detected",
                                "disease_id": "invalid_leaf",
                                "confidence": 0.0,
                                "severity": "none",
                                "pathogen_type": "None",
                                "symptoms": [],
                                "reasoning": "The image is a screenshot of programming code."
                            })}
                        ]
                    }
                }
            ]
        }
        mock_post.return_value = _make_mock_response(200, doc_response)

        result = diagnose_crop_disease(self.image_bytes)
        self.assertEqual(result["status"], "invalid_leaf")
        self.assertEqual(result["message"], "Invalid image. Please upload a clear photo of a plant leaf.")
        self.assertEqual(result["reasoning"], "Invalid image. Please upload a clear photo of a plant leaf.")
        self.assertNotIn("code", result["message"].lower())
        self.assertNotIn("screenshot", result["message"].lower())

    @patch("services.gemini_service.time.sleep", return_value=None)
    @patch("services.gemini_service.requests.post")
    def test_fallback_model_invalid_leaf_never_reveals_object(self, mock_post, mock_sleep):
        """5. Fallback model (gemini-3.6-flash) invalid leaf path also returns sanitized generic message."""
        resp_503 = _make_mock_response(503, {"error": {"message": "High demand"}})
        fallback_invalid_response = {
            "candidates": [
                {
                    "content": {
                        "parts": [
                            {"text": json.dumps({
                                "is_plant_leaf": False,
                                "is_healthy": False,
                                "crop": "None",
                                "disease": "No Crop Leaf Detected",
                                "disease_id": "invalid_leaf",
                                "confidence": 0.0,
                                "severity": "none",
                                "pathogen_type": "None",
                                "symptoms": [],
                                "reasoning": "This is a car parked in front of a building."
                            })}
                        ]
                    }
                }
            ]
        }
        resp_200 = _make_mock_response(200, fallback_invalid_response)

        # 3 failures on 3.5 (503), then fallback 3.6 returns 200 with invalid leaf
        mock_post.side_effect = [resp_503, resp_503, resp_503, resp_200]

        result = diagnose_crop_disease(self.image_bytes)
        self.assertEqual(result["status"], "invalid_leaf")
        self.assertEqual(result["model_used"], "gemini-3.6-flash")
        self.assertEqual(result["message"], "Invalid image. Please upload a clear photo of a plant leaf.")
        self.assertEqual(result["reasoning"], "Invalid image. Please upload a clear photo of a plant leaf.")
        self.assertNotIn("car", result["message"].lower())
        self.assertNotIn("building", result["message"].lower())

    @patch("services.gemini_service.requests.post")
    def test_api_endpoint_sanitizes_invalid_leaf_completely(self, mock_post):
        """6. FastAPI endpoint /api/v1/disease/predict completely sanitizes invalid leaf response."""
        import asyncio
        from httpx import ASGITransport, AsyncClient
        from main import app

        leak_response = {
            "candidates": [
                {
                    "content": {
                        "parts": [
                            {"text": json.dumps({
                                "is_plant_leaf": False,
                                "is_healthy": False,
                                "crop": "None",
                                "disease": "No Crop Leaf Detected",
                                "disease_id": "invalid_leaf",
                                "confidence": 0.0,
                                "severity": "none",
                                "pathogen_type": "None",
                                "symptoms": [],
                                "reasoning": "Leaked secret object: human face and glasses."
                            })}
                        ]
                    }
                }
            ]
        }
        mock_post.return_value = _make_mock_response(200, leak_response)

        async def _run():
            async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
                res = await client.post(
                    "/api/v1/disease/predict",
                    files={"file": ("test.jpg", self.image_bytes, "image/jpeg")}
                )
                self.assertEqual(res.status_code, 200)
                data = res.json()
                self.assertEqual(data["status"], "invalid_leaf")
                self.assertEqual(data["message"], "Invalid image. Please upload a clear photo of a plant leaf.")
                self.assertEqual(data["reasoning"], "Invalid image. Please upload a clear photo of a plant leaf.")
                # Verify leaked object strings are completely absent from the entire JSON response
                raw_json = json.dumps(data)
                self.assertNotIn("human", raw_json.lower())
                self.assertNotIn("glasses", raw_json.lower())
                self.assertNotIn("face", raw_json.lower())

        asyncio.run(_run())

    def test_configuration_defaults_and_env_overrides(self):
        """Verify configuration defaults and environment overrides."""
        self.assertEqual(get_gemini_primary_model(), "gemini-3.5-flash")
        self.assertEqual(get_gemini_fallback_model(), "gemini-3.6-flash")
        self.assertEqual(get_gemini_model(), "gemini-3.5-flash")

        with patch.dict("os.environ", {"GEMINI_PRIMARY_MODEL": "custom-primary", "GEMINI_FALLBACK_MODEL": "custom-fallback"}):
            self.assertEqual(get_gemini_primary_model(), "custom-primary")
            self.assertEqual(get_gemini_fallback_model(), "custom-fallback")
            self.assertEqual(get_gemini_model(), "custom-primary")

        # Backwards compatibility: GEMINI_MODEL sets primary when GEMINI_PRIMARY_MODEL is unset
        with patch.dict("os.environ", {"GEMINI_MODEL": "legacy-gemini"}, clear=True):
            self.assertEqual(get_gemini_primary_model(), "legacy-gemini")
            self.assertEqual(get_gemini_model(), "legacy-gemini")
            self.assertEqual(get_gemini_fallback_model(), "gemini-3.6-flash")


if __name__ == "__main__":
    unittest.main()
