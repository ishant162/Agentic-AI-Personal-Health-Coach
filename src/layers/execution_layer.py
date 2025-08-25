from langchain_core.messages import SystemMessage, HumanMessage


from src.tools.execution_tools import get_tools


def execute_actions(actions, patient_id, llm):
    """
    Execute the actions given
    """
    tools = get_tools()
    llm_with_tools = llm.bind_tools(tools)
    prompt = f"""
    You are a healthcare assistant. The patient requires intervention based on
    the following actions: {actions}.

    Please:
    1. Use the available tools to update the EHR for Patient_ID {patient_id}.
    2. Schedule a follow-up appointment for Patient_ID {patient_id}.
    3. Notify the care team about Patient_ID {patient_id}.

    After completing these tasks, provide a brief summary of what actions were
    taken and confirm their completion.
    """
    messages = [
        SystemMessage(
            content="You are a helpful healthcare assistant. "
            "Always summarize the actions you take."
        ),
        HumanMessage(content=prompt)
    ]
    response = llm_with_tools.invoke(messages)
    return [response]
