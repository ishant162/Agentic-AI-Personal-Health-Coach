from typing_extensions import TypedDict, Optional


class State(TypedDict):
    """
    Represent the structure of the state used in graph.
    """
    user_input: str  # Required
    parsed_input: Optional[str]
    inference_decision: Optional[str]
    ehr_data: Optional[dict]
    engineered_prompt: Optional[str]
    risk_score: Optional[int]
    action_plan: Optional[str]
    execution_result: Optional[str]
    llm_response: Optional[str]
