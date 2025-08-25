import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
load_dotenv()

api_key = os.environ.get("GENERATIVE_ENGINE_API_KEY")


class OpenAILLM:
    """
    OpenAI LLM wrapper for interacting with the OpenAI API.
    """

    def __init__(self):
        self.api_key = api_key

    def get_llm_model(self) -> ChatOpenAI:
        """
        Get the OpenAI LLM model based on user input.

        Returns:
            ChatOpenAI: An instance of the OpenAI LLM model.
        """
        llm = ChatOpenAI(
            openai_api_base="https://api.generative.engine.capgemini.com/v1",
            openai_api_key=api_key,  # This is required but can be any string
            model_name="openai.gpt-4o",  # Specify the OpenAI model
            default_headers={"x-api-key": api_key},
            temperature=0.7
        )
        return llm
