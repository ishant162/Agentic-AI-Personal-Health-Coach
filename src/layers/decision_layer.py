"""Decision Layer Module"""

import json
import re

from src.state.state import InferenceDecision


def fallback_decision(user_input: str) -> InferenceDecision:
    """Fallback decision logic if LLM fails."""
    symptoms_keywords = [
        "pain",
        "hurt",
        "ache",
        "fever",
        "nausea",
        "dizzy",
        "bleeding",
        "swelling",
        "rash",
        "cough",
        "shortness of breath",
        "chest pain",
        "headache",
        "vomiting",
        "diarrhea",
    ]

    has_symptoms = any(keyword in user_input.lower() for keyword in symptoms_keywords)

    if has_symptoms:
        return InferenceDecision(
            decision="Negative",
            confidence=0.7,
            reasoning="Detected potential symptoms using keyword matching (fallback)",
        )

    return InferenceDecision(
        decision="Positive",
        confidence=0.6,
        reasoning="No clear symptoms detected using keyword matching (fallback)",
    )


def llm_inference_decision(user_input: str, llm) -> InferenceDecision:
    """
    Use LLM to make intelligent inference decisions based on user input.
    """

    system_prompt = """You are a medical triage assistant. Analyze the user's
    input and decide whether they need:

    - "Positive": Direct LLM response (for general health questions, no symptoms,
    wellness inquiries, or low-risk scenarios)
    - "Negative": EHR data retrieval (for symptom reporting, specific health concerns,
    or cases requiring medical history)
    
    Consider factors like:
    - Presence of symptoms
    - Urgency indicators
    - Need for personalized medical data
    - Risk assessment
    
    You MUST respond with valid JSON in exactly this format:
    {
        "decision": "Positive" or "Negative",
        "confidence": float between 0.0 and 1.0,
        "reasoning": "your explanation here"
    }
    
    Do not include any text before or after the JSON."""

    user_prompt = f"""
    Analyze this health-related input and make a routing decision:
    
    User Input: "{user_input}"
    
    Determine whether this requires EHR data access or can be handled with a direct response.
    
    Respond with only valid JSON in the specified format."""

    # Using structured output with the LLM
    try:
        response = llm.with_structured_output(InferenceDecision).invoke(
            [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ]
        )

        print(
            f"LLM Decision: {response.decision} (confidence: {response.confidence:.2f})"
        )
        print(f"Reasoning: {response.reasoning}")

        return response

    except Exception as e:
        print(f"Error in LLM decision making: {e}")
        # Try manual JSON parsing as backup
        try:
            return parse_llm_response_manually(user_input, llm)
        except Exception as e2:
            print(f"Manual parsing also failed: {e2}")
            return fallback_decision(user_input)


def parse_llm_response_manually(user_input: str, llm) -> InferenceDecision:
    """Manually parse LLM response if structured output fails."""

    system_prompt = """You are a medical triage assistant. Analyze the user's input and decide:
    
    - "Positive": Direct LLM response (general questions, no symptoms)
    - "Negative": EHR data needed (symptoms, specific concerns)
    
    Respond with ONLY a JSON object:
    {"decision": "Positive", "confidence": 0.8, "reasoning": "explanation"}"""

    user_prompt = f'Input: "{user_input}"\n\nRespond with JSON only:'

    response = llm.invoke(
        [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ]
    )

    # Extract JSON from response
    response_text = response.content if hasattr(response, "content") else str(response)

    # Try to find JSON in the response
    json_match = re.search(r"\{.*\}", response_text, re.DOTALL)
    if json_match:
        json_str = json_match.group()
        try:
            parsed = json.loads(json_str)
            return InferenceDecision(**parsed)
        except (json.JSONDecodeError, TypeError) as e:
            raise ValueError(f"Invalid JSON structure: {e}")

    raise ValueError("No JSON found in response")


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
