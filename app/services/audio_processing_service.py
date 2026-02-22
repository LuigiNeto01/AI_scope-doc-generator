try:
    from app.services.audio_extraction_service import AudioExtractionService
except ModuleNotFoundError:
    from audio_extraction_service import AudioExtractionService


class AudioProcessingService:
    def __init__(
        self,
        output_dir: str = "data/audio",
    ):
        self.extractor = AudioExtractionService(output_dir=output_dir)

    def extrair_audio(self, caminho_video: str) -> str:
        return self.extractor.extrair_audio(caminho_video)


if __name__ == "__main__":
    caminho_video = (r"D:\Trabalho\POC_IA-Document\data\Video.mp4")
    output_dir = "data/audio"

    service = AudioProcessingService(output_dir=output_dir)
    caminho_audio = service.extrair_audio(caminho_video)

    print(f"Audio gerado: {caminho_audio}")
