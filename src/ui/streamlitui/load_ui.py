"""Streamlit UI Loader Module"""

import streamlit as st


class LoadStreamlitUI:
    """
    Load the Streamlit UI components with Tailwind-inspired styling.
    """

    def __init__(self):
        self.title = "🩺 Personal AI Health Coach"

    def load_ui(self):
        """
        Load the Streamlit UI components.
        Returns:
            Tuple[str, int]: user_input and patient_id
        """
        st.set_page_config(
            page_title=self.title,
            page_icon="🧠",
            layout="centered"
        )
        # Tailwind-inspired styling
        st.markdown("""
            <style>
                html, body, [data-testid="stAppViewContainer"] {
                    height: 100%;
                    margin: 0;
                    padding: 0;
                    background: linear-gradient(
                        to bottom right,s
                        #ffffff,
                        #a3d5f7
                    );
                    background-attachment: fixed;
                    font-family: 'Segoe UI', sans-serif;
                    color: #1f2937;
                }

                [data-testid="stAppViewContainer"] > div:first-child {
                    padding: 2rem;
                }

                .stTextArea textarea, .stTextInput input {
                    background-color: #ffffff;
                    border-radius: 0.75rem;
                    padding: 0.75rem;
                    color: #111827;
                    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.25);
                    border: 1px solid #d1d5db;
                    transition: all 0.3s ease-in-out;
                }

                .stTextArea textarea:hover, .stTextInput input:hover {
                    box-shadow: 0 6px 18px rgba(0, 0, 0, 0.35);
                    border-color: #60a5fa;
                }

                .stButton button {
                    background-color: #3b82f6;
                    color: white;
                    border-radius: 0.75rem;
                    padding: 0.6em 1.2em;
                    font-weight: 600;
                    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.25);
                    border: none;
                    transition: all 0.3s ease-in-out;
                }

                .stButton button:hover {
                    background-color: #2563eb;
                    box-shadow: 0 6px 18px rgba(0, 0, 0, 0.35);
                }

                .chat-bubble {
                    background-color: #e0f2ff;
                    color: #1f2937;
                    padding: 1rem;
                    border-radius: 1rem;
                    margin-top: 1.5rem;
                    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.25);
                    max-width: 90%;
                    font-size: 1rem;
                    line-height: 1.6;
                    animation: fadeIn 0.5s ease-in-out;
                }

                @keyframes fadeIn {
                    from { opacity: 0; transform: translateY(10px); }
                    to { opacity: 1; transform: translateY(0); }
                }
            </style>
        """, unsafe_allow_html=True)

        st.markdown(f"# {self.title}")
        st.markdown(
            "Welcome! Please enter your health query and patient ID below."
        )

        with st.form("health_form"):
            user_input = st.text_area(
                "📝 Describe your symptoms or health query:",
                placeholder="e.g., I feel tired and my chest feels heavy",
                height=150
            )

            patient_id = st.text_input(
                "🆔 Enter Patient ID:",
                placeholder="e.g., 1024"
            )

            submitted = st.form_submit_button("🚀 Submit Query")

        if submitted:
            if not user_input.strip():
                st.warning("⚠️ Please enter a valid health query.")
                return None, None
            if not patient_id.strip().isdigit():
                st.warning("⚠️ Patient ID must be a number.")
                return None, None

            st.success("✅ Input received. Processing your query...")
            return user_input.strip(), int(patient_id.strip())

        return None, None
