"""Classe base para inicializar e reutilizar o cliente OpenAI nos servicos de IA."""

import os
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

from app.core.constants import OPENAI_API_KEY_ENV
from app.core.exceptions import MissingAPIKeyError


class BaseAI:
    """Classe base para servicos que usam o cliente OpenAI."""

    def __init__(self, api_key: str = None):
        """Inicializa o cliente OpenAI usando API key explicita ou variavel de ambiente."""
        env_path = Path(__file__).resolve().parents[3] / ".env"
        load_dotenv(dotenv_path=env_path)

        resolved_api_key = api_key or os.getenv(OPENAI_API_KEY_ENV)
        if not resolved_api_key:
            raise MissingAPIKeyError(
                f"{OPENAI_API_KEY_ENV} nao encontrada. Defina no .env ou passe api_key."
            )

        self.client = OpenAI(api_key=resolved_api_key)

    def generate(self, model: str, messages: list, temperature: float = 0.2):
        """Executa uma chamada de chat completion e retorna apenas o texto da resposta."""
        response = self.client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=temperature
        )

        return response.choices[0].message.content
