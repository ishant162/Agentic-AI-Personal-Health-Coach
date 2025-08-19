def inference_decision(input):
    """
    Checks if inferencing and ehr data fetching is necessary based
    on the input.
    """
    if "no symptoms" in input.lower():
        return "Positive"
    else:
        return "Negative"
