from .base_ai import BaseAI


class GenerativeService(BaseAI):

    def gerar_texto(self, prompt: str, model: str = "gpt-4o-mini"):
        messages = [
            {"role": "system", "content": "Você é um assistente técnico especializado."},
            {"role": "user", "content": prompt}
        ]

        return self.generate(model=model, messages=messages)
