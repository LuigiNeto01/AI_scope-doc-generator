from .base_ai import BaseAI

class TranscriptionService(BaseAI):

    def transcrever_audio(self, modelo: str, caminho_audio: str) -> str:
        with open(caminho_audio, "rb") as audio_file:
            transcript = self.client.audio.transcriptions.create(
                model=modelo,
                file=audio_file
            )

        return transcript.text
