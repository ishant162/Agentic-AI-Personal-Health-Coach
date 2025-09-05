"""Main Module"""

import streamlit as st
import time

from src.ui.streamlitui.load_ui import LoadStreamlitUI
from src.llm.openai_llm import OpenAILLM
from src.graph.graph_builder import GraphBuilder


def load_health_agent():
    """Load and build the health agent components via Streamlit UI."""

    # Initialize session state for patient ID and chat history
    if "patient_id" not in st.session_state:
        st.session_state.patient_id = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    ui = LoadStreamlitUI()
    user_input, patient_id = ui.load_ui()

    # Set patient ID only once
    if patient_id and st.session_state.patient_id is None:
        st.session_state.patient_id = patient_id

    if user_input and st.session_state.patient_id:
        with st.spinner("🧠 Thinking... Processing your query..."):
            llm = OpenAILLM().get_llm_model()
            graph_builder = GraphBuilder(llm)
            graph = graph_builder.setup_graph()

            response = graph.invoke({
                "user_input": user_input,
                "patient_id": st.session_state.patient_id
            })

        # Save to chat history
        st.session_state.chat_history.append({
            "query": user_input,
            "response": response['llm_response']
        })

    # Inject chat bubble styling
    st.markdown("""
        <style>
            .chat-bubble {
                background-color: #e0f2ff;
                color: #1f2937;
                padding: 1rem;
                border-radius: 1rem;
                margin-top: 1rem;
                box-shadow: 0 4px 12px rgba(0, 0, 0, 0.25);
                max-width: 90%;
                font-size: 1rem;
                line-height: 1.6;
                animation: fadeIn 0.5s ease-in-out;
                white-space: pre-wrap;
            }

            .user-query {
                background-color: #dbeafe;
                padding: 0.75rem;
                border-radius: 1rem;
                margin-top: 1rem;
                box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
                font-weight: 500;
            }

            @keyframes fadeIn {
                from { opacity: 0; transform: translateY(10px); }
                to { opacity: 1; transform: translateY(0); }
            }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("### 💬 Conversation")

    # Display chat history with typing effect for latest response
    for i, chat in enumerate(st.session_state.chat_history):
        st.markdown(
            f"<div class='user-query'>🧑‍⚕️ You: {chat['query']}</div>",
            unsafe_allow_html=True
        )

        if i == len(st.session_state.chat_history) - 1:
            bubble = st.empty()
            typed_text = ""
            for char in chat['response']:
                typed_text += char
                bubble.markdown(
                    f"<div class='chat-bubble'>{typed_text}</div>",
                    unsafe_allow_html=True
                )
                time.sleep(0.01)
        else:
            st.markdown(
                f"<div class='chat-bubble'>{chat['response']}</div>",
                unsafe_allow_html=True
            )
