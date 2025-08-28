"""State Module"""

from typing_extensions import TypedDict, Optional, List
from pandas.core.frame import DataFrame
from langchain_core.messages import BaseMessage


class State(TypedDict):
    """
    Represent the structure of the state used in graph.
    """
    user_input: str  # Required
    patient_id: int  # Required
    messages: Optional[List[BaseMessage]]
    parsed_input: Optional[str]
    inference_decision: Optional[str]
    ehr_data: Optional[dict]
    engineered_prompt: DataFrame
    risk_score: Optional[int]
    action_plan: Optional[list]
    llm_response: Optional[str]
