import os

from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

groq_api_key = os.environ.get("GROQ_API_KEY")


class GroqLLM:
    """
    Groq LLM wrapper for interacting with the Groq API.
    """

    def __init__(self):
        self.api_key = groq_api_key

    def get_llm_model(self) -> ChatGroq:
        """
        Get the Groq LLM model based on user input.

        Returns:
            ChatGroq: An instance of the Groq LLM model.
        """
        llm = ChatGroq(model="llama3-8b-8192", groq_api_key=self.api_key)

        return llm
