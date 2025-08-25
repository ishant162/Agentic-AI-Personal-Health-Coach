import pandas as pd


def parse_user_input(llm, user_input):
    """
    Parses the user input and converts symptoms into a JSON-like dictionary.
    """

    prompt = f"""
    You are a medical assistant. Extract symptoms from the following user
    input and return them as a JSON dictionary. Each symptom should be a key
    with a boolean value `true` indicating its presence.

    User input: "{user_input}"

    Example output:
    {{
        "fatigue": true,
        "poor_sleep": true
    }}
    Only include symptoms mentioned in the input. Do not infer or add
    extra symptoms.

    If there are no concerning symptoms mentioned, respond with the string:
    "no symptoms": true

    The output should be just the JSON dictionary strictly. The output should
    be strictly formatted as JSON.
    """

    response = llm.invoke(prompt)

    # Extract and return the JSON-like dictionary from the response
    return response.content


def generate_inference_prompt(ehr_data):
    """
    Generates the inference prompt for calculating the risk score
    """
    evaluator_data = pd.DataFrame([ehr_data])
    return evaluator_data
