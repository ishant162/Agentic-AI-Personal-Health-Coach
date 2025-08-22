from typing_extensions import TypedDict, Optional
from pandas.core.frame import DataFrame


class State(TypedDict):
    """
    Represent the structure of the state used in graph.
    """
    user_input: str  # Required
    patient_id: str  # Required
    parsed_input: Optional[str]
    inference_decision: Optional[str]
    ehr_data: Optional[dict]
    engineered_prompt: DataFrame
    risk_score: Optional[int]
    action_plan: Optional[list]
    execution_result: Optional[str]
    llm_response: Optional[str]
