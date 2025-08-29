"""State Module"""

from typing import Literal
from typing_extensions import TypedDict, Optional, List
from pandas.core.frame import DataFrame
from langchain_core.messages import BaseMessage
from pydantic import BaseModel


class InferenceDecision(BaseModel):
    """Structured output for inference decision."""
    decision: Literal["Positive", "Negative"]
    confidence: float
    reasoning: str


class State(TypedDict):
    """
    Represent the structure of the state used in graph.
    """
    user_input: str  # Required
    patient_id: int  # Required
    messages: Optional[List[BaseMessage]]
    parsed_input: Optional[str]
    inference_decision: Optional[InferenceDecision]
    ehr_data: Optional[dict]
    engineered_prompt: DataFrame
    risk_score: Optional[int]
    action_plan: Optional[list]
    llm_response: Optional[str]
