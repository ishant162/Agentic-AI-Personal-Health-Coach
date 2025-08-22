from src.tools.execution_tools import get_tools


def execute_actions(actions, llm):
    """
    Execute the actions given
    """
    if "no_symptoms" in actions:
        return "No action needed, patient is healthy."
    else:
        llm_tools = llm.bind_tools(get_tools())
        llm_tools.invoke(actions)
