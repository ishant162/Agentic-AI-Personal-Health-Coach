import streamlit as st

from src.ui.streamlitui.load_ui import LoadStreamlitUI
from src.llm.groq_llm import GroqLLM
from src.graph.graph_builder import GraphBuilder


def load_health_agent():
    # LoadUI
    ui = LoadStreamlitUI()
    user_input = ui.load_ui()

    if not user_input:
        st.error("No user input provided. Please select options from the sidebar.")
        return

    llm = GroqLLM().get_llm_model()
    graph_builder = GraphBuilder(llm)
    graph = graph_builder.health_agent_workflow()
