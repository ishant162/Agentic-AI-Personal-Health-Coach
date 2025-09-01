"""EHR Data Retrieval Module"""

import pandas as pd


def get_ehr_data(patient_id) -> dict:
    """
    Retrieves Electronic Health Record (EHR) data for a specific patient
    from a CSV database.

    This function loads the EHR dataset from a predefined CSV file, filters
    the data based on the provided patient ID, and returns the patient's
    record as a dictionary.

    Args:
        patient_id (int): The unique identifier of the patient whose EHR
            data is to be retrieved.

    Returns:
        dict: A dictionary containing the patient's EHR data if found.
            Returns None if the patient ID does not exist in the dataset.
    """
    # Load the dataset
    df = pd.read_csv('./src/ehr_database/ehr_data.csv')
    # Filter the row with the given Patient_ID
    patient_data = df[df['Patient_ID'] == patient_id]
    # Check if patient exists
    if patient_data.empty:
        return None  # or raise an exception or return a message
    # Convert the row to a dictionary
    return patient_data.iloc[0].to_dict()
