"""Servico de transcricao de audio para texto usando modelos de speech-to-text."""

from .base_ai import BaseAI


class TranscriptionService(BaseAI):
    """Servico de transcricao de audio com modelos de speech-to-text."""

    def transcrever_audio(self, modelo: str, caminho_audio: str) -> str:
        """Transcreve o arquivo de audio informado e retorna o texto resultante."""
        # A API de transcricao requer stream binario aberto do arquivo de audio.
        with open(caminho_audio, "rb") as audio_file:
            transcript = self.client.audio.transcriptions.create(
                model=modelo,
                file=audio_file
            )

        # Mantemos apenas o texto plano para consumo pelos proximos servicos.
        return transcript.text
