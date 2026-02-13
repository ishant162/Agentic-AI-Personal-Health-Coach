"""OpenAI LLM Module"""

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
            model="openai.gpt-5.1",  # Specify the OpenAI model you want to use
            base_url="https://openai.generative.engine.capgemini.com/v1",
            api_key=api_key,
            default_headers={"x-api-key": api_key}  # Some implementations require this header
        )
        return llm
