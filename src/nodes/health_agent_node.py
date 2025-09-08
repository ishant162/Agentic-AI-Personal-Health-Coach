"""Health Agent Node Module"""

from src.state.state import State
from src.layers.prompt_engineering_layer import (
    parse_user_input,
    generate_inference_prompt
)
from src.layers.decision_layer import llm_inference_decision, next_action
from src.layers.inference_layer import inference_on_patient_data
from src.layers.execution_layer import execute_actions
from src.tools.get_ehr_data import get_ehr_data


class HealthAgentNode:
    """Health Agent Node for processing health-related queries."""

    def __init__(self, model):
        """
        Initializes the Health Agent Node with the given LLM model.

        Args:
            model: The language model instance to be used.
        """
        self.llm = model

    # Node definitions
    def input_parser(self, state: State) -> State:
        """
        Parses user input and extracts relevant information.

        Args:
            state (State): The current state containing user input.

        Returns:
            State: Updated state with parsed input.
        """
        print("Parsing user input...")
        state["parsed_input"] = parse_user_input(
            self.llm, state.get('user_input', '')
        )
        return state

    def llm_responder(self, state: State) -> State:
        """
        Generates a response from the LLM based on the execution result.

        Args:
            state (State): The current state containing execution results.

        Returns:
            State: Updated state with LLM response.
        """
        print("Generating LLM response...")
        llm = self.llm
        action_plan = state.get("action_plan", "")

        prompt = f"""
        You are a friendly and professional medical assistant.

        Here is a summary of the patient's current health-related actions:
        {action_plan}

        Please analyze this summary and generate a short, empathetic message
        for the patient:
        - If the actions suggest no concerning symptoms (e.g., "no_symptoms"),
            reassure the patient warmly.
        - If the actions suggest follow-up steps (e.g., "schedule_appointment"
            , "notify_care_team", "update_ehr"), explain them clearly and
            kindly.
        - Always keep the tone supportive, respectful, and easy to understand.
        - Do not include any technical terms or internal instructions—just a
            patient-facing message.

        Examples:
        Healthy: "Great news! Based on your recent health check, everything
        looks good. You're in great shape. Keep taking care of yourself,
        and don't hesitate to reach out if anything changes."

        Concern: "We've identified a few things that may need attention. We've
        taken steps to ensure you're well cared for. Please follow up with your
        care team, and remember we're here to support you."

        Respond with just the message.
        """
        response = llm.invoke(prompt)
        state["llm_response"] = response.content

        return state

    def prompt_engineer(self, state: State) -> State:
        """
        Engineers the prompt for the Inference Model

        Args:
            state (State): The current state containing EHR data.

        Returns:
            State: Updated state with engineered prompt.
        """
        print("Engineering prompt with EHR data...")
        state["engineered_prompt"] = generate_inference_prompt(
            state["ehr_data"]
        )
        return state

    def risk_evaluator(self, state: State) -> State:
        """
        Evaluates the health risk based on the engineered prompt.

        Args:
            state (State): The current state containing the engineered prompt.

        Returns:
            State: Updated state with risk score.
        """
        print("Evaluating health risk...")
        state["risk_score"] = inference_on_patient_data(
            state["engineered_prompt"]
        )
        return state

    def inference_decision(self, state: State) -> str:
        """
        Makes a decision based on the inference results using LLM.

        Args:
            state (State): The current state containing parsed input.

        Returns:
            str: The decision made by the LLM.
        """
        print("Planning next steps based on risk assessment...")

        parsed_input = state.get("parsed_input", '')
        result = llm_inference_decision(
            parsed_input, self.llm
        )

        # Store the full decision context as a dict in state
        state["inference_decision"] = {
            "decision": result.decision,
            "confidence": result.confidence,
            "reasoning": result.reasoning
        }

        return result.decision

    def decision_planner(self, state: State) -> State:
        """
        Plans the next steps based on the risk score.

        Args:
            state (State): The current state containing the risk score.

        Returns:
            State: Updated state with action plan.
        """
        print("Planning next steps based on risk score...")
        state["action_plan"] = next_action(state["risk_score"])
        return state

    def decision_planner_node(self, state: State) -> str:
        """
        Determines the next node in the decision planning process.

        Args:
            state (State): The current state containing the action plan.

        Returns:
            str: The next node to transition to ("Positive" or "Negative").
        """
        if "no_symptoms" in state.get("action_plan", []):
            return "Negative"
        else:
            return "Positive"

    def execution_manager(self, state: State) -> State:
        """
        Executes the planned actions.

        Args:
            state (State): The current state containing the action plan.

        Returns:
            State: Updated state with execution messages.
        """
        print("Executing planned actions...")
        state["messages"] = execute_actions(
            state["action_plan"], state["patient_id"], self.llm
        )
        return state

    def ehr_connector(self, state: State) -> State:
        """
        Fetches EHR data for the patient.

        Args:
            state (State): The current state containing patient ID.

        Returns:
            State: Updated state with EHR data.
        """
        print("Fetching EHR data...")
        state["ehr_data"] = get_ehr_data(state["patient_id"])
        return state
