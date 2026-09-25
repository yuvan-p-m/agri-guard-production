"""
AgriGuard SMS Service Layer — Fast2SMS Integration
Single source of truth for all SMS dispatching across FastAPI endpoints and APScheduler jobs.
"""

import os
import logging
from typing import Any, Dict, Optional, Union
import requests
from dotenv import load_dotenv

logger = logging.getLogger(__name__)

# Ensure .env is loaded if not already
load_dotenv()

FAST2SMS_ENDPOINT = "https://www.fast2sms.com/dev/bulkV2"


def get_fast2sms_api_key() -> str:
    """
    Retrieve Fast2SMS API Key from environment.
    Checks FAST2SMS_API_KEY first, with fallback to SMS_API_KEY.
    Does NOT use hardcoded expired keys.
    """
    key = os.getenv("FAST2SMS_API_KEY") or os.getenv("SMS_API_KEY") or ""
    return key.strip()


def validate_and_clean_indian_mobile(phone: Any) -> Optional[str]:
    """
    Validates and standardizes an Indian mobile number.
    Strips country code (+91/91), spaces, hyphens, and leading zeros.
    Returns clean 10-digit number if valid (10 digits starting with 6, 7, 8, or 9),
    or None if invalid.
    """
    if not phone:
        return None

    raw_str = str(phone).strip().replace(" ", "").replace("-", "")

    # Strip country code / leading zeros
    if raw_str.startswith("+91"):
        raw_str = raw_str[3:]
    elif raw_str.startswith("91") and len(raw_str) == 12:
        raw_str = raw_str[2:]
    elif raw_str.startswith("0") and len(raw_str) == 11:
        raw_str = raw_str[1:]

    digits = "".join(c for c in raw_str if c.isdigit())
    if len(digits) == 10 and digits[0] in "6789":
        return digits

    return None


def clean_mobile_number(raw_mobile: Any) -> str:
    """
    Backward-compatible helper for existing imports.
    """
    cleaned = validate_and_clean_indian_mobile(raw_mobile)
    return cleaned or ""


def send_sms_detailed(mobile: Any, message: str) -> Dict[str, Any]:
    """
    Dispatches SMS via Fast2SMS Quick SMS API (route 'q') with strict validation,
    meaningful error categorization, and safe logging.

    Returns structured dictionary:
    {
        "success": bool,
        "status": "sent" | "failed",
        "error_type": Optional[str],  # 'config_error' | 'validation_error' | 'provider_error' | 'network_error'
        "message": str,                # Informative, safe status message
        "phone": str,                  # Cleaned 10-digit mobile number
        "provider_code": Optional[int] # Fast2SMS internal code or HTTP status
    }
    """
    clean_phone = validate_and_clean_indian_mobile(mobile)
    if not clean_phone:
        logger.warning(f"SMS dispatch skipped: invalid Indian mobile number '{mobile}'")
        return {
            "success": False,
            "status": "failed",
            "error_type": "validation_error",
            "message": f"Invalid Indian mobile number '{mobile}'. Must be a 10-digit number starting with 6, 7, 8, or 9.",
            "phone": str(mobile) if mobile else "",
            "provider_code": 400
        }

    clean_msg = str(message or "").strip()
    if not clean_msg:
        return {
            "success": False,
            "status": "failed",
            "error_type": "validation_error",
            "message": "SMS message cannot be empty.",
            "phone": clean_phone,
            "provider_code": 400
        }

    api_key = get_fast2sms_api_key()
    if not api_key:
        logger.error("Fast2SMS API key is not configured in backend environment (FAST2SMS_API_KEY)")
        return {
            "success": False,
            "status": "failed",
            "error_type": "config_error",
            "message": "Fast2SMS API key is not configured. Please set FAST2SMS_API_KEY in the backend environment.",
            "phone": clean_phone,
            "provider_code": 503
        }

    # Split into 160-character chunks if needed
    chunks = [clean_msg[i:i + 160] for i in range(0, len(clean_msg), 160)]
    headers = {
        "authorization": api_key,
        "Content-Type": "application/json"
    }

    last_provider_msg = "SMS sent successfully"
    last_status_code = 200

    for chunk in chunks:
        payload = {
            "route": "q",
            "message": chunk,
            "language": "english",
            "flash": 0,
            "numbers": clean_phone
        }

        try:
            res = requests.post(
                FAST2SMS_ENDPOINT,
                json=payload,
                headers=headers,
                timeout=12
            )

            # Try parsing JSON response from Fast2SMS
            try:
                res_data = res.json()
            except Exception:
                res_data = {}

            if res.status_code == 200:
                is_returned = res_data.get("return", False)
                raw_msg = res_data.get("message", "No response message")
                if isinstance(raw_msg, list):
                    provider_msg = ", ".join(str(m) for m in raw_msg)
                else:
                    provider_msg = str(raw_msg)

                if is_returned:
                    logger.info(f"Fast2SMS message delivered successfully to {clean_phone}")
                    last_provider_msg = provider_msg
                else:
                    logger.warning(f"Fast2SMS rejected dispatch to {clean_phone}: {provider_msg}")
                    return {
                        "success": False,
                        "status": "failed",
                        "error_type": "provider_error",
                        "message": provider_msg,
                        "phone": clean_phone,
                        "provider_code": res_data.get("status_code", 400)
                    }
            else:
                raw_msg = res_data.get("message", res.text)
                if isinstance(raw_msg, list):
                    provider_msg = ", ".join(str(m) for m in raw_msg)
                else:
                    provider_msg = str(raw_msg)

                logger.error(f"Fast2SMS HTTP {res.status_code} for {clean_phone}: {provider_msg}")
                return {
                    "success": False,
                    "status": "failed",
                    "error_type": "provider_error",
                    "message": provider_msg or f"Fast2SMS returned HTTP {res.status_code}",
                    "phone": clean_phone,
                    "provider_code": res.status_code
                }

        except requests.exceptions.Timeout:
            logger.error(f"Fast2SMS request timed out for mobile {clean_phone}")
            return {
                "success": False,
                "status": "failed",
                "error_type": "network_error",
                "message": "Fast2SMS gateway request timed out. Please try again.",
                "phone": clean_phone,
                "provider_code": 504
            }
        except requests.exceptions.RequestException as req_err:
            logger.error(f"Fast2SMS network connection failed: {req_err}")
            return {
                "success": False,
                "status": "failed",
                "error_type": "network_error",
                "message": "Unable to reach Fast2SMS gateway. Please check network connectivity.",
                "phone": clean_phone,
                "provider_code": 502
            }
        except Exception as e:
            logger.error(f"Unexpected SMS dispatch exception: {e}")
            return {
                "success": False,
                "status": "failed",
                "error_type": "internal_error",
                "message": f"Unexpected error during SMS dispatch: {str(e)}",
                "phone": clean_phone,
                "provider_code": 500
            }

    return {
        "success": True,
        "status": "sent",
        "message": clean_msg,
        "phone": clean_phone,
        "provider_code": last_status_code
    }


def send_sms(mobile: Any, message: str) -> bool:
    """
    Simplified boolean dispatch helper for backward compatibility.
    """
    result = send_sms_detailed(mobile, message)
    return result.get("success", False)
