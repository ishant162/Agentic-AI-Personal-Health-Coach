import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq
load_dotenv()

api_key = os.environ.get("GROQ_API")


class GroqLLM:
    """
    Groq LLM wrapper for interacting with the Groq API.
    """

    def __init__(self):
        self.api_key = api_key

    def get_llm_model(self) -> ChatGroq:
        """
        Get the Groq LLM model based on user input.

        Returns:
            ChatGroq: An instance of the Groq LLM model.
        """
        llm = ChatGroq(model="llama3-8b-8192", groq_api_key=self.api_key)

        return llm
