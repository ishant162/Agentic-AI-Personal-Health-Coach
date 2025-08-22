import pandas as pd


def get_ehr_data(patient_id):
    """
    Gets EHR data for a specific patient.
    """
    # Load the dataset
    df = pd.read_csv('heart_with_patient_id.csv')
    # Filter the row with the given Patient_ID
    patient_data = df[df['Patient_ID'] == patient_id]
    # Check if patient exists
    if patient_data.empty:
        return None  # or raise an exception or return a message
    # Convert the row to a dictionary
    return patient_data.iloc[0].to_dict()
