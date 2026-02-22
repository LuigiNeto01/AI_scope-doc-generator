"""Facade de processamento de audio para simplificar uso na pipeline."""

try:
    # Import padrao quando executado como pacote.
    from app.services.audio_extraction_service import AudioExtractionService
except ModuleNotFoundError:
    # Fallback para execucao direta do arquivo.
    from audio_extraction_service import AudioExtractionService

from app.core.constants import DEFAULT_AUDIO_DIR, DEFAULT_VIDEO_PATH


class AudioProcessingService:
    """Facade para rotinas de processamento de audio."""

    def __init__(
        self,
        output_dir: str = str(DEFAULT_AUDIO_DIR),
    ):
        """Configura o extrator de audio com o diretorio de saida informado."""
        self.extractor = AudioExtractionService(output_dir=output_dir)

    def extrair_audio(self, caminho_video: str) -> str:
        """Extrai o audio do video informado e retorna o caminho do arquivo gerado."""
        # Mantem a API simples para a camada de pipeline.
        return self.extractor.extrair_audio(caminho_video)


if __name__ == "__main__":
    caminho_video = str(DEFAULT_VIDEO_PATH)
    output_dir = str(DEFAULT_AUDIO_DIR)

    service = AudioProcessingService(output_dir=output_dir)
    caminho_audio = service.extrair_audio(caminho_video)

    print(f"Audio gerado: {caminho_audio}")
