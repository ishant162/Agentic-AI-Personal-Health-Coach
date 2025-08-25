from src.tools.execution_tools import get_tools, create_tool_node


def execute_actions(actions, llm):
    """
    Execute the actions given
    """
    if "no_symptoms" in actions:
        return "No action needed, patient is healthy."
    else:
        tools = get_tools()
        tool_node = create_tool_node(tools)

