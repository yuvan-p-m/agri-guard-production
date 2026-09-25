import os
import json
import logging
import firebase_admin
from firebase_admin import credentials, firestore, auth

logger = logging.getLogger(__name__)

_firebase_app = None
_db = None
_is_initialized = False

def init_firebase():
    """
    Initialize Firebase Admin SDK safely.
    Supports:
      1. FIREBASE_SERVICE_ACCOUNT_JSON (Production/Render): Raw service account JSON string.
      2. FIREBASE_SERVICE_ACCOUNT_KEY (Local Dev): Path to service account JSON file.
    Safely reuses existing default app if already initialized.
    """
    global _firebase_app, _db, _is_initialized
    if _firebase_app is not None and _is_initialized:
        return _firebase_app

    # Check if a default Firebase app is already initialized in firebase_admin
    try:
        _firebase_app = firebase_admin.get_app()
        if _db is None:
            _db = firestore.client()
        _is_initialized = True
        logger.info("Reusing existing initialized Firebase Admin app.")
        return _firebase_app
    except ValueError:
        # No default app exists yet; proceed with initialization
        pass
    except Exception as e:
        logger.warning(f"Notice while checking existing Firebase Admin app: {e}")

    enable_fb = os.getenv("ENABLE_FIREBASE", "true").lower() in ("true", "1", "yes")
    if not enable_fb:
        logger.info("Firebase initialization skipped (ENABLE_FIREBASE is false).")
        _is_initialized = False
        return None

    service_account_json = os.getenv("FIREBASE_SERVICE_ACCOUNT_JSON")
    cred = None

    if service_account_json and service_account_json.strip():
        try:
            service_account_info = json.loads(service_account_json.strip())
            cred = credentials.Certificate(service_account_info)
            logger.info("Parsed Firebase credentials from FIREBASE_SERVICE_ACCOUNT_JSON environment variable.")
        except json.JSONDecodeError as json_err:
            logger.error(f"Failed to parse FIREBASE_SERVICE_ACCOUNT_JSON as JSON: {json_err}")
            _is_initialized = False
            return None
        except Exception as cred_err:
            logger.error(f"Failed to load Firebase credentials from FIREBASE_SERVICE_ACCOUNT_JSON: {cred_err}")
            _is_initialized = False
            return None
    else:
        cred_path = os.getenv("FIREBASE_SERVICE_ACCOUNT_KEY", "serviceAccountKey.json")
        resolved_path = None

        if os.path.exists(cred_path):
            resolved_path = cred_path
        elif not os.path.isabs(cred_path):
            # Check relative to backend root directory
            backend_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
            alt_path = os.path.join(backend_dir, cred_path)
            if os.path.exists(alt_path):
                resolved_path = alt_path

        if resolved_path and os.path.exists(resolved_path):
            try:
                cred = credentials.Certificate(resolved_path)
                logger.info(f"Loaded Firebase credentials from file: {resolved_path}")
            except Exception as cred_err:
                logger.error(f"Failed to initialize Firebase Admin with key '{resolved_path}': {cred_err}")
                _is_initialized = False
                return None
        else:
            logger.info(
                f"No Firebase credentials found (FIREBASE_SERVICE_ACCOUNT_JSON not set and file '{cred_path}' not found). "
                "Running with mock DB fallback."
            )
            _is_initialized = False
            return None

    try:
        _firebase_app = firebase_admin.initialize_app(cred)
        _db = firestore.client()
        _is_initialized = True
        logger.info("Firebase Admin initialized successfully.")
    except ValueError as val_err:
        if "The default Firebase app already exists" in str(val_err):
            try:
                _firebase_app = firebase_admin.get_app()
                _db = firestore.client()
                _is_initialized = True
                logger.info("Default Firebase app already existed; reused successfully.")
            except Exception as get_err:
                logger.error(f"Failed to retrieve existing Firebase Admin app: {get_err}")
                _is_initialized = False
        else:
            logger.error(f"ValueError during Firebase Admin initialization: {val_err}")
            _is_initialized = False
    except Exception as e:
        logger.error(f"Failed to initialize Firebase Admin SDK: {e}")
        _is_initialized = False

    return _firebase_app

def is_firebase_initialized() -> bool:
    global _is_initialized, _firebase_app
    return bool(_is_initialized and _firebase_app is not None)

def get_firestore_db():
    """
    Get Firestore DB client instance.
    """
    global _db
    if _db is None and is_firebase_initialized():
        try:
            _db = firestore.client()
        except Exception as e:
            logger.error(f"Failed to get Firestore client: {e}")
    elif _db is None:
        init_firebase()
    return _db

# Attempt initialization at import time
init_firebase()
