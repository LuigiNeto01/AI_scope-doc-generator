"""Servico de geracao textual orientado a prompts para construir secoes de escopo."""

from .base_ai import BaseAI
from app.core.constants import DEFAULT_SYSTEM_PROMPT, DEFAULT_TEXT_MODEL


class GenerativeService(BaseAI):
    """Servico para geracao de texto via modelo conversacional."""

    def gerar_texto(self, prompt: str, model: str = DEFAULT_TEXT_MODEL):
        """Gera texto tecnico a partir do prompt informado."""
        messages = [
            {"role": "system", "content": DEFAULT_SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ]

        return self.generate(model=model, messages=messages)
