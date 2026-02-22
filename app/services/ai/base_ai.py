import os
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

class BaseAI:
    def __init__(self, api_key: str = None):
        env_path = Path(__file__).resolve().parents[3] / ".env"
        load_dotenv(dotenv_path=env_path)

        resolved_api_key = api_key or os.getenv("OPENAI_API_KEY")
        if not resolved_api_key:
            raise ValueError(
                "OPENAI_API_KEY nao encontrada. Defina no .env ou passe api_key."
            )

        self.client = OpenAI(api_key=resolved_api_key)

    def generate(self, model: str, messages: list, temperature: float = 0.2):
        response = self.client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=temperature
        )

        return response.choices[0].message.content
