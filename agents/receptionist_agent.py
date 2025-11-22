from utils.db import get_patient

def receptionist_flow(name: str):
    patient = get_patient(name)
    if not patient:
        return None, "I couldn't find your discharge report. Check your name."

    msg = (
        f"Hi {patient['patient_name']}! I found your report.\n"
        f"Diagnosis: {patient['primary_diagnosis']}\n"
        "How are you feeling today?"
    )
    return patient, msg
