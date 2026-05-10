"""Health Tracking Tools Module"""

from datetime import datetime

def log_vital_sign(patient_id: int, vital_type: str, value: str, unit: str) -> str:
    """
    Simulates logging a new vital sign for the patient.
    In a real scenario, this would update a database.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    # Simulation: return a success message
    return f"Successfully logged {vital_type}: {value} {unit} for patient {patient_id} at {timestamp}"

def log_medication_intake(patient_id: int, med_name: str) -> str:
    """
    Simulates logging medication intake for the patient.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    return f"Confirmed: {med_name} taken by patient {patient_id} at {timestamp}"

def get_proactive_follow_ups(patient_id: int) -> list:
    """
    Simulates retrieving pending follow-up tasks for a patient.
    """
    # Mock data for simulation
    mock_follow_ups = {
        101: ["Check post-op incision for redness", "Review morning blood sugar log"],
        102: ["Assess fatigue levels", "Confirm physical therapy appointment"]
    }
    return mock_follow_ups.get(patient_id, ["General wellness check-in"])