import tensorflow as tf


def inference_on_patient_data(patient_ehr_data):
    """
    Infers the health risk score based on the patient's EHR data.
    """
    model = tf.keras.models.load_model('inference_model.h5')
    # Run inference
    prediction = model.predict(patient_ehr_data)
    # Interpret the result
    return prediction[0][0]
