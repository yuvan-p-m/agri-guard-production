"""
Unit and integration tests for AgriGuard SMS Scheduler Removal & Manual SMS Endpoints.

Verifies:
1. Automatic 4-times daily SMS scheduler has been completely removed.
2. backend/scheduler.py is deleted and APScheduler is not imported or registered at startup.
3. No automatic SMS are sent during backend startup.
4. APScheduler is removed from requirements.txt.
5. Manual SMS endpoints (/alerts/subscribe, /alerts/send-weather-alert, /alerts/send-test-sms)
   remain fully operational and call send_sms_detailed().
6. Fast2SMS validation and helper functions remain intact.
"""

import sys
import os
import unittest
from pathlib import Path
from unittest.mock import patch, MagicMock

# Ensure backend/ and backend/app/ are on sys.path
BACKEND_DIR = Path(__file__).resolve().parent.parent
BACKEND_APP_DIR = BACKEND_DIR / "app"
for p in [str(BACKEND_DIR), str(BACKEND_APP_DIR)]:
    if p not in sys.path:
        sys.path.insert(0, p)

from app.main import app
from sms_service import (
    validate_and_clean_indian_mobile,
    send_sms_detailed,
    get_fast2sms_api_key
)
from fastapi.testclient import TestClient


class TestSMSSchedulerRemoval(unittest.TestCase):
    """Verifies that the automated SMS scheduler is completely gone."""

    def test_scheduler_file_does_not_exist(self):
        """scheduler.py must be deleted from the backend root and app directories."""
        root_scheduler = BACKEND_DIR / "scheduler.py"
        app_scheduler = BACKEND_APP_DIR / "scheduler.py"
        self.assertFalse(root_scheduler.exists(), f"{root_scheduler} should have been deleted!")
        self.assertFalse(app_scheduler.exists(), f"{app_scheduler} should not exist!")

    def test_scheduler_cannot_be_imported(self):
        """Attempting to import scheduler must raise ModuleNotFoundError."""
        with self.assertRaises(ModuleNotFoundError):
            import scheduler  # noqa: F401

    def test_apscheduler_removed_from_requirements(self):
        """requirements.txt must not contain APScheduler."""
        req_path = BACKEND_DIR / "requirements.txt"
        self.assertTrue(req_path.exists())
        content = req_path.read_text()
        self.assertNotIn("APScheduler", content, "APScheduler should not be in requirements.txt")
        self.assertNotIn("apscheduler", content.lower(), "apscheduler should not be in requirements.txt")

    @patch("sms_service.send_sms_detailed")
    def test_startup_does_not_send_sms_or_start_scheduler(self, mock_send_sms):
        """
        Starting the FastAPI application should:
        1. NOT call send_sms_detailed()
        2. NOT start or register any APScheduler jobs
        3. NOT log 'Fast2SMS 4-times daily cron scheduler started.'
        """
        import inspect
        import asyncio
        startup_funcs = app.router.on_startup
        for fn in startup_funcs:
            if inspect.iscoroutinefunction(fn):
                asyncio.run(fn())
            else:
                fn()

        # No automatic SMS should be dispatched at startup
        mock_send_sms.assert_not_called()

    def test_main_py_does_not_mention_scheduler(self):
        """main.py must not contain imports or startup calls for scheduler."""
        main_path = BACKEND_APP_DIR / "main.py"
        content = main_path.read_text()
        self.assertNotIn("from scheduler import", content)
        self.assertNotIn("start_scheduler", content)
        self.assertNotIn("Fast2SMS 4-times daily cron scheduler started.", content)


class TestManualSMSEndpoints(unittest.TestCase):
    """Verifies that manual/explicit SMS API endpoints work as intended."""

    def setUp(self):
        # Using Starlette's direct test client or ASGI handler
        # To avoid starlette/httpx version mismatch issues, we call router handlers directly
        # and test with FastAPI dependency injection.
        pass

    def test_phone_validation(self):
        """Verifies Indian mobile phone validation logic."""
        self.assertEqual(validate_and_clean_indian_mobile("9876543210"), "9876543210")
        self.assertEqual(validate_and_clean_indian_mobile("+919876543210"), "9876543210")
        self.assertEqual(validate_and_clean_indian_mobile("919876543210"), "9876543210")
        self.assertEqual(validate_and_clean_indian_mobile("09876543210"), "9876543210")
        self.assertEqual(validate_and_clean_indian_mobile(" 98765-43210 "), "9876543210")

        # Invalid numbers
        self.assertIsNone(validate_and_clean_indian_mobile("12345"))
        self.assertIsNone(validate_and_clean_indian_mobile("5555555555"))  # Doesn't start with 6-9
        self.assertIsNone(validate_and_clean_indian_mobile("abcdefghij"))
        self.assertIsNone(validate_and_clean_indian_mobile(""))

    @patch("app.api.alerts.send_sms_detailed")
    def test_subscribe_endpoint_success(self, mock_send_sms):
        """POST /alerts/subscribe must call send_sms_detailed and return status subscribed."""
        from app.api.alerts import subscribe_to_alerts, SubscribePayload
        import asyncio

        mock_send_sms.return_value = {
            "success": True,
            "status": "sent",
            "message": "SMS dispatched successfully",
            "phone": "9876543210"
        }

        payload = SubscribePayload(
            phone="9876543210",
            crop="Wheat",
            alert_types=["weather_warning"]
        )

        res = asyncio.run(subscribe_to_alerts(payload))
        self.assertEqual(res["status"], "subscribed")
        self.assertEqual(res["phone"], "9876543210")
        self.assertEqual(res["crop"], "Wheat")
        self.assertTrue(res["sms_sent"])

        mock_send_sms.assert_called_once()
        args, _ = mock_send_sms.call_args
        self.assertEqual(args[0], "9876543210")
        self.assertIn("Wheat", args[1])

    @patch("app.api.alerts.send_sms_detailed")
    def test_subscribe_endpoint_invalid_phone(self, mock_send_sms):
        """POST /alerts/subscribe with invalid phone must raise 400 and NOT call send_sms_detailed."""
        from app.api.alerts import subscribe_to_alerts, SubscribePayload
        from fastapi import HTTPException
        import asyncio

        payload = SubscribePayload(phone="12345")
        with self.assertRaises(HTTPException) as ctx:
            asyncio.run(subscribe_to_alerts(payload))

        self.assertEqual(ctx.exception.status_code, 400)
        mock_send_sms.assert_not_called()

    @patch("app.api.alerts.send_sms_detailed")
    def test_send_weather_alert_endpoint_success(self, mock_send_sms):
        """POST /alerts/send-weather-alert must call send_sms_detailed with weather advisory."""
        from app.api.alerts import send_weather_alert, WeatherAlertPayload
        import asyncio

        mock_send_sms.return_value = {
            "success": True,
            "status": "sent",
            "message": "Delivered",
            "phone": "9876543210"
        }

        payload = WeatherAlertPayload(
            phone="9876543210",
            alert_message="Heavy rainfall expected in Nagpur within 24 hours."
        )

        res = asyncio.run(send_weather_alert(payload))
        self.assertTrue(res["success"])
        self.assertEqual(res["status"], "sent")
        self.assertEqual(res["phone"], "9876543210")
        self.assertIn("Heavy rainfall expected", res["message"])

        mock_send_sms.assert_called_once()
        args, _ = mock_send_sms.call_args
        self.assertEqual(args[0], "9876543210")
        self.assertIn("WEATHER ALERT:", args[1])

    @patch("app.api.alerts.send_sms_detailed")
    def test_send_weather_alert_invalid_phone(self, mock_send_sms):
        """POST /alerts/send-weather-alert with invalid phone must raise 400 and NOT call send_sms_detailed."""
        from app.api.alerts import send_weather_alert, WeatherAlertPayload
        from fastapi import HTTPException
        import asyncio

        payload = WeatherAlertPayload(phone="invalid_phone", alert_message="Storm warning")
        with self.assertRaises(HTTPException) as ctx:
            asyncio.run(send_weather_alert(payload))

        self.assertEqual(ctx.exception.status_code, 400)
        mock_send_sms.assert_not_called()

    @patch("app.api.alerts.send_sms_detailed")
    def test_send_test_sms_endpoint_success(self, mock_send_sms):
        """POST /alerts/send-test-sms must generate climate/sensor summary and call send_sms_detailed."""
        from app.api.alerts import send_test_sms_endpoint, TestSmsPayload
        import asyncio

        mock_send_sms.return_value = {
            "success": True,
            "status": "sent",
            "message": "Delivered",
            "phone": "9876543210"
        }

        payload = TestSmsPayload(
            phone="9876543210",
            name="Ramesh",
            location="Nagpur"
        )

        res = asyncio.run(send_test_sms_endpoint(payload))
        self.assertTrue(res["success"])
        self.assertEqual(res["status"], "sent")
        self.assertEqual(res["phone"], "9876543210")

        mock_send_sms.assert_called_once()
        args, _ = mock_send_sms.call_args
        self.assertEqual(args[0], "9876543210")
        self.assertIn("Good Morning Ramesh!", args[1])

    @patch("app.api.alerts.send_sms_detailed")
    def test_send_test_sms_missing_phone(self, mock_send_sms):
        """POST /alerts/send-test-sms with missing phone must raise 400."""
        from app.api.alerts import send_test_sms_endpoint, TestSmsPayload
        from fastapi import HTTPException
        import asyncio

        payload = TestSmsPayload(phone=None, uid=None)
        with self.assertRaises(HTTPException) as ctx:
            asyncio.run(send_test_sms_endpoint(payload))

        self.assertEqual(ctx.exception.status_code, 400)
        mock_send_sms.assert_not_called()


if __name__ == "__main__":
    unittest.main()
