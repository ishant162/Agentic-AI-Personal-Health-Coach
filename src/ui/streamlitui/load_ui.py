"""Streamlit UI Loader Module"""

import streamlit as st


class LoadStreamlitUI:
    """
    Load the Streamlit UI components for the health coach app.
    """

    def __init__(self):
        self.title = "Agentic AI Health Coach"

    def load_ui(self):
        """
        Load the Streamlit UI components.
        """
        # App title
        st.title(self.title)

        # Input field for user symptoms
        user_input = st.text_area(
            "Describe your symptoms:",
            placeholder="e.g., I feel tired and my chest feels heavy",
        )

        # Submit button
        if st.button("Submit"):
            if user_input.strip():
                st.success("Input received. Processing...")
                # Here you would send `user_input` to your LangGraph backend
                # For now, just display it
                st.write("You said:", user_input)
            else:
                st.warning("Please enter your symptoms before submitting.")

        return user_input
