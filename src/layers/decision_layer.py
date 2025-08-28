"""Decision Layer Module"""

def inference_decision(inp):
    """
    Checks if inferencing and ehr data fetching is necessary based
    on the input.
    """
    if "no symptoms" in inp.lower():
        return "Positive"
    else:
        return "Negative"


def next_action(risk_score):
    """
    Determines the next action based on the risk score.
    """
    if risk_score > 0.5:
        return ["schedule_appointment", "notify_care_team", "update_ehr"]
    else:
        return ["no_symptoms"]
