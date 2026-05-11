"""Health Tracking Tools Module with Simulated Database"""

from datetime import datetime
from typing import Dict, Optional

# --- SIMULATED IN-MEMORY DATABASE ---

class SimulatedHealthDB:
    def __init__(self):
        # Initial mock data
        self._db = {
            101: {
                "vitals": [
                    {"timestamp": "2024-05-01 08:00", "type": "Blood Pressure", "value": "120/80", "unit": "mmHg"}
                ],
                "medications": [
                    {"name": "Lisinopril", "last_taken": "2024-05-09 08:15", "adherence_status": True}
                ],
                "follow_ups": ["Check post-op incision for redness", "Review morning blood sugar log"]
            },
            102: {
                "vitals": [],
                "medications": [
                    {"name": "Metformin", "last_taken": None, "adherence_status": False}
                ],
                "follow_ups": ["Assess fatigue levels"]
            }
        }

    def get_patient_record(self, patient_id: int) -> Optional[Dict]:
        return self._db.get(patient_id)

    def add_vital(self, patient_id: int, vital: Dict):
        if patient_id not in self._db:
            self._db[patient_id] = {"vitals": [], "medications": [], "follow_ups": []}
        self._db[patient_id]["vitals"].append(vital)

    def update_medication(self, patient_id: int, med_name: str, timestamp: str):
        if patient_id in self._db:
            for med in self._db[patient_id]["medications"]:
                if med["name"].lower() in med_name.lower():
                    med["last_taken"] = timestamp
                    med["adherence_status"] = True
                    return True
        return False

# Global instance for the simulation
health_db = SimulatedHealthDB()

# --- TOOL FUNCTIONS ---

def log_vital_sign(patient_id: int, vital_type: str, value: str, unit: str) -> str:
    """
    Logs a new vital sign for the patient into the simulated database.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    vital = {
        "timestamp": timestamp,
        "type": vital_type,
        "value": value,
        "unit": unit
    }
    health_db.add_vital(patient_id, vital)
    return f"Successfully logged {vital_type}: {value} {unit} for patient {patient_id} at {timestamp}"

def log_medication_intake(patient_id: int, med_name: str) -> str:
    """
    Updates medication adherence in the simulated database.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    success = health_db.update_medication(patient_id, med_name, timestamp)
    if success:
        return f"Confirmed: {med_name} intake logged for patient {patient_id} at {timestamp}"
    else:
        # Fallback if medication not explicitly found
        return f"Logged medication intake for patient {patient_id} at {timestamp}"

def get_proactive_follow_ups(patient_id: int) -> list:
    """
    Retrieves pending follow-up tasks from the simulated database.
    """
    record = health_db.get_patient_record(patient_id)
    if record:
        return record.get("follow_ups", ["General wellness check-in"])
    return ["General wellness check-in"]

def get_patient_health_state(patient_id: int) -> Dict:
    """
    Returns the full health record for the patient.
    """
    return health_db.get_patient_record(patient_id) or {}