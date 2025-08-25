import streamlit as st

from src.ui.streamlitui.load_ui import LoadStreamlitUI
from src.llm.groq_llm import GroqLLM
from src.llm.openai_llm import OpenAILLM
from src.graph.graph_builder import GraphBuilder


def load_health_agent():
    # LoadUI
    # ui = LoadStreamlitUI()
    user_input = input("Please enter your health-related query: ")
    patient_id = int(input("Please enter the Patient ID: "))

    llm = OpenAILLM().get_llm_model()
    graph_builder = GraphBuilder(llm)
    graph = graph_builder.setup_graph()
    response = graph.invoke({
        "user_input": user_input,
        "patient_id": patient_id
    })
    print(response.items())
