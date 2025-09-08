"""Execution Tools Module"""

import pandas as pd

from langgraph.prebuilt import ToolNode
from langchain.tools import tool


@tool
def update_ehr(patient_id: int) -> None:
    """
    Updates the EHR data for a specific patient.

    Args:
        patient_id (int): The ID of the patient whose EHR data is
            to be updated.
    """

    # Load the dataset
    df = pd.read_csv('./src/ehr_database/ehr_data.csv')

    # Check if the patient_id exists
    if patient_id in df['Patient_ID'].values:
        # Increment the readmission field by 1
        df.loc[df['Patient_ID'] == patient_id, 'readmission'] += 1

        # Save the updated dataset
        df.to_csv('./src/ehr_database/ehr_data.csv', index=False)
        print(f"Readmission count updated for Patient_ID {patient_id}.")
    else:
        print(f"Patient_ID {patient_id} not found in the dataset.")


@tool
def schedule_appointment(patient_id: int) -> None:
    """
    Schedules a follow-up appointment for the patient.

    Args:
        patient_id (int): The ID of the patient.
    """
    print(f"Scheduling appointment for Patient_ID {patient_id}...")


@tool
def notify_care_team(patient_id: int) -> None:
    """
    Notifies the care team about the patient's status.

    Args:
        patient_id (int): The ID of the patient.
    """
    print(f"Notifying care team for Patient_ID {patient_id}...")


def get_tools() -> list:
    """
    Returns a list of available tools for the patient.

    Returns:
        list: A list of tool names.
    """
    return [update_ehr, schedule_appointment, notify_care_team]


def create_tool_node(tools) -> ToolNode:
    """
    Create a tool node for the graph.
    This function initializes a ToolNode with the provided tools
    and returns it.

    Args:
        tools (list): A list of tool functions.

    Returns:
        ToolNode: An instance of ToolNode containing the tools.
    """
    return ToolNode(tools=tools)
