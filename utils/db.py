import json
import os

# def get_patient(name: str):
#     with open("data/patients.json") as f:
#         patients = json.load(f)
#     matches = [p for p in patients if p["patient_name"].lower() == name.lower()]
#     if not matches:
#         return None
#     return matches[0]


DATA_FILE = "data/patients.json"

def get_patient(name: str):
    # If file missing → return None safely
    if not os.path.exists(DATA_FILE):
        return None
    
    # If file is empty → return None safely
    if os.path.getsize(DATA_FILE) == 0:
        return None

    try:
        with open(DATA_FILE) as f:
            patients = json.load(f)
    except json.JSONDecodeError:
        print("⚠ JSON file corrupted or empty!")
        return None

    matches = [p for p in patients if p["patient_name"].lower() == name.lower()]
    return matches[0] if matches else None
