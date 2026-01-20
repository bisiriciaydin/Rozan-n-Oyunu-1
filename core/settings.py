# core/settings.py
import json
import os

SETTINGS_PATH = os.path.join("data", "settings.json")


def load_settings():
    if not os.path.exists(SETTINGS_PATH):
        return {
            "music_on": True,
            "music_random": True,
            "music_file": None
        }

    try:
        with open(SETTINGS_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {
            "music_on": True,
            "music_random": True,
            "music_file": None
        }


def save_settings(settings: dict):
    os.makedirs("data", exist_ok=True)
    with open(SETTINGS_PATH, "w", encoding="utf-8") as f:
        json.dump(settings, f, ensure_ascii=False, indent=2)
