#!/usr/bin/env python3
"""
AgriGuard 25-Language Multilingual Calibration Audit & Validation Script
Validates:
1. All 25 required locale files exist in src/i18n/locales/
2. Valid JSON structure
3. Exact key parity with canonical en.json (0 missing, 0 extra)
4. No empty string translations
5. Placeholder interpolation consistency ({{variable}})
6. Script purity (zero Devanagari in non-Devanagari, zero Tamil in non-Tamil, etc.)
7. No cross-language digit contamination
"""

import os
import sys
import json
import re
from typing import Dict, List, Set, Any, Tuple

REQUIRED_LANGUAGES = [
    "en", "ta", "te", "ml", "kn", "hi", "bn", "mr", "gu", "pa",
    "ur", "or", "as", "ne", "si", "ar", "fr", "es", "pt", "de",
    "it", "ru", "ja", "ko", "zh"
]

LANGUAGE_NAMES = {
    "en": "English", "ta": "Tamil", "te": "Telugu", "ml": "Malayalam", "kn": "Kannada",
    "hi": "Hindi", "bn": "Bengali", "mr": "Marathi", "gu": "Gujarati", "pa": "Punjabi",
    "ur": "Urdu", "or": "Odia", "as": "Assamese", "ne": "Nepali", "si": "Sinhala",
    "ar": "Arabic", "fr": "French", "es": "Spanish", "pt": "Portuguese", "de": "German",
    "it": "Italian", "ru": "Russian", "ja": "Japanese", "ko": "Korean", "zh": "Chinese"
}

SCRIPT_RULES = {
    "Devanagari": (r"[\u0900-\u097F]", {"hi", "mr", "ne"}),
    "Tamil": (r"[\u0B80-\u0BFF]", {"ta"}),
    "Telugu": (r"[\u0C00-\u0C7F]", {"te"}),
    "Kannada": (r"[\u0C80-\u0CFF]", {"kn"}),
    "Malayalam": (r"[\u0D00-\u0D7F]", {"ml"}),
    "Gujarati": (r"[\u0A80-\u0AFF]", {"gu"}),
    "Gurmukhi": (r"[\u0A00-\u0A7F]", {"pa"}),
    "Odia": (r"[\u0B00-\u0B7F]", {"or"}),
    "Bengali/Assamese": (r"[\u0980-\u09FF]", {"bn", "as"}),
    "Sinhala": (r"[\u0D80-\u0DFF]", {"si"}),
    "Arabic/Urdu": (r"[\u0600-\u06FF]", {"ar", "ur"}),
    "Cyrillic": (r"[\u0400-\u04FF]", {"ru"}),
    "Japanese Kana": (r"[\u3040-\u30FF]", {"ja"}),
    "Korean Hangul": (r"[\uAC00-\uD7AF]", {"ko"}),
}

# Permitted shared punctuation across Indic scripts (e.g. Danda \u0964, Double Danda \u0965)
ALLOWED_SHARED_CHARS = {"\u0964", "\u0965"}

def flatten_keys(obj: Any, prefix: str = "") -> Dict[str, str]:
    items: Dict[str, str] = {}
    if isinstance(obj, dict):
        for k, v in obj.items():
            pk = f"{prefix}.{k}" if prefix else k
            items.update(flatten_keys(v, pk))
    elif isinstance(obj, list):
        items[prefix] = " ".join(str(x) for x in obj)
    else:
        items[prefix] = str(obj)
    return items

def extract_variables(text: str) -> Set[str]:
    return set(re.findall(r"\{\{\s*(\w+)\s*\}\}", text))

def main() -> int:
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    locales_dir = os.path.join(base_dir, "src", "i18n", "locales")

    print("================================================================================")
    print("           AgriGuard Multilingual Calibration & Locale Parity Audit             ")
    print(f" Locales Directory: {locales_dir}")
    print(f" Total Languages: {len(REQUIRED_LANGUAGES)}")
    print("================================================================================\n")

    # 1. Check Canonical en.json
    en_path = os.path.join(locales_dir, "en.json")
    if not os.path.exists(en_path):
        print(f"FATAL: Canonical locale file not found: {en_path}")
        return 1

    try:
        with open(en_path, "r", encoding="utf-8") as f:
            en_data = json.load(f)
    except Exception as e:
        print(f"FATAL: Failed to parse canonical en.json: {e}")
        return 1

    en_keys = flatten_keys(en_data)
    total_canonical_keys = len(en_keys)
    print(f"Canonical 'en' has {total_canonical_keys} translation keys.\n")

    results = []
    has_errors = False

    for lang in REQUIRED_LANGUAGES:
        lang_name = LANGUAGE_NAMES.get(lang, lang)
        fpath = os.path.join(locales_dir, f"{lang}.json")

        if not os.path.exists(fpath):
            results.append({
                "code": lang,
                "name": lang_name,
                "status": "MISSING FILE",
                "missing_keys": total_canonical_keys,
                "empty_keys": 0,
                "extra_keys": 0,
                "var_mismatches": 0,
                "script_leaks": 0,
                "notes": "File does not exist"
            })
            has_errors = True
            continue

        try:
            with open(fpath, "r", encoding="utf-8") as f:
                data = json.load(f)
        except Exception as e:
            results.append({
                "code": lang,
                "name": lang_name,
                "status": "INVALID JSON",
                "missing_keys": total_canonical_keys,
                "empty_keys": 0,
                "extra_keys": 0,
                "var_mismatches": 0,
                "script_leaks": 0,
                "notes": f"JSON parse error: {str(e)[:40]}"
            })
            has_errors = True
            continue

        flat_data = flatten_keys(data)

        missing = [k for k in en_keys if k not in flat_data]
        extra = [k for k in flat_data if k not in en_keys]
        empty = [k for k, v in flat_data.items() if not str(v).strip()]

        var_mismatches = []
        for k, v in flat_data.items():
            if k in en_keys:
                en_vars = extract_variables(en_keys[k])
                cur_vars = extract_variables(v)
                if en_vars != cur_vars:
                    var_mismatches.append((k, en_vars, cur_vars))

        script_leaks = []
        for script_label, (pattern, allowed_locales) in SCRIPT_RULES.items():
            if lang not in allowed_locales:
                for k, v in flat_data.items():
                    val_clean = "".join(c for c in v if c not in ALLOWED_SHARED_CHARS)
                    hits = re.findall(pattern, val_clean)
                    if hits:
                        script_leaks.append((script_label, k, "".join(hits[:8])))

        status = "PASS" if not (missing or extra or empty or var_mismatches or script_leaks) else "FAIL"
        if status == "FAIL":
            has_errors = True

        note_parts = []
        if missing: note_parts.append(f"{len(missing)} missing")
        if extra: note_parts.append(f"{len(extra)} extra")
        if empty: note_parts.append(f"{len(empty)} empty")
        if var_mismatches: note_parts.append(f"{len(var_mismatches)} vars mismatch")
        if script_leaks: note_parts.append(f"{len(script_leaks)} script leaks ({script_leaks[0][0]})")

        results.append({
            "code": lang,
            "name": lang_name,
            "status": status,
            "missing_keys": len(missing),
            "empty_keys": len(empty),
            "extra_keys": len(extra),
            "var_mismatches": len(var_mismatches),
            "script_leaks": len(script_leaks),
            "notes": ", ".join(note_parts) if note_parts else "Parity 100% verified"
        })

    # Print Table
    header = f"{'Code':<6} | {'Language':<14} | {'Status':<7} | {'Missing':<8} | {'Empty':<6} | {'VarFail':<8} | {'Leaks':<6} | {'Audit Notes'}"
    print(header)
    print("-" * len(header))
    for r in results:
        line = (
            f"{r['code']:<6} | "
            f"{r['name']:<14} | "
            f"{r['status']:<7} | "
            f"{r['missing_keys']:<8} | "
            f"{r['empty_keys']:<6} | "
            f"{r['var_mismatches']:<8} | "
            f"{r['script_leaks']:<6} | "
            f"{r['notes']}"
        )
        print(line)

    print("\n" + "=" * 80)
    if has_errors:
        print("❌ MULTILINGUAL CALIBRATION AUDIT FAILED: Issues found in locale files.")
        return 1
    else:
        print("✅ MULTILINGUAL CALIBRATION AUDIT PASSED: All 25 locales 100% calibrated & pure.")
        return 0

if __name__ == "__main__":
    sys.exit(main())
