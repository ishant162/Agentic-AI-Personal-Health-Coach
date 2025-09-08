"""Inference Layer Module"""

import tensorflow as tf


def inference_on_patient_data(patient_ehr_data) -> float:
    """
    Infers the health risk score based on the patient's EHR data.

    Args:
        patient_ehr_data: Preprocessed EHR data for the patient.

    Returns:
        float: The inferred risk score between 0 and 1.
    """
    model = tf.keras.models.load_model(
        './src/prediction_model/inference_model.h5'
    )
    # Run inference
    patient_ehr_data = patient_ehr_data.drop(
        ['target', 'Patient_ID', 'readmission'], axis=1
    )
    prediction = model.predict(patient_ehr_data)
    # Interpret the result
    return float(prediction[0][0])
