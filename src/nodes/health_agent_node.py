from src.state.state import State
from src.layers.prompt_engineering_layer import (
    parse_user_input, 
    generate_inference_prompt
)
from src.layers.decision_layer import inference_decision, next_action
from src.layers.inference_layer import inference_on_patient_data
from src.layers.execution_layer import execute_actions
from src.tools.get_ehr_data import get_ehr_data


class HealthAgentNode:
    """Health Agent Node for processing health-related queries."""

    def __init__(self, model):
        self.llm = model

    # Node definitions
    def input_parser(self, state: State) -> State:
        """
        Parses user input and extracts relevant information.
        """
        print("Parsing user input...")
        state["parsed_input"] = parse_user_input(
            self.llm, state.get('user_input', '')
        )
        return state

    def llm_responder(self, state: State) -> State:
        """
        Generates a response from the LLM based on the parsed input.
        """
        print("Generating LLM response...")
        llm = self.llm
        user_input = state.get("user_input", "")

        # if state.get("inference_decision") == "Positive":
        prompt = f"""
        You are a friendly and professional medical assistant. Based on 
        the analysis, the patient has no concerning symptoms.

        Here is the patient's input:
        "{user_input}"

        Please generate a short, reassuring message to let the patient 
        know they are perfectly fine and healthy. The tone should be warm,
        supportive, and clear.

        Example:
        "Great news! Based on your input, there are no concerning symptoms.
        You seem to be in good health.
        Keep taking care of yourself and feel free to reach out if
        anything changes."

        Respond with just the message.
        """
        response = llm.invoke(prompt)
        state["llm_response"] = response.content

        return state

    def prompt_engineer(self, state: State) -> State:
        print("Engineering prompt with EHR data...")
        state["engineered_prompt"] = generate_inference_prompt(
            state["ehr_data"]
        )
        return state

    def risk_evaluator(self, state: State) -> State:
        print("Evaluating health risk...")
        state["risk_score"] = inference_on_patient_data(
            state["engineered_prompt"]
        )
        return state

    def inference_decision_node(self, state: State) -> State:
        print("Planning next steps based on risk score...")
        result = inference_decision(
            state.get("parsed_input", '')
        )
        state["inference_decision"] = result
        return result

    def decision_planner(self, state: State) -> State:
        print("Planning next steps based on risk score...")
        state["action_plan"] = next_action(state["risk_score"])
        return state

    def execution_manager(self, state: State) -> State:
        print("Executing planned actions...")
        state["execution_result"] = execute_actions(
            state["action_plan"], self.llm
        )
        return state

    def ehr_connector(self, state: State) -> State:
        print("Fetching EHR data...")
        state["ehr_data"] = get_ehr_data(state["patient_id"])
        return state
