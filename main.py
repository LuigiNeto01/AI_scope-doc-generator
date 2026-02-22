import logging
from pathlib import Path

from app.services.audio_processing_service import AudioProcessingService
from app.services.project_scope_service import ProjectScopeService
from app.services.ai.transcription_service import TranscriptionService

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
)
logger = logging.getLogger(__name__)

def main() -> None:

    caminho_video = r"D:\Trabalho\POC_IA-Document\data\Video.mp4"
    output_dir = "data/audio"
    caminho_transcricao = Path("data/transcricao/audio_transcrito.txt")

    logger.info("Iniciando pipeline")
    logger.info("Extraindo audio do video: %s", caminho_video)
    audio_service = AudioProcessingService(output_dir=output_dir)
    caminho_audio = audio_service.extrair_audio(caminho_video)
    logger.info("Audio extraido em: %s", caminho_audio)

    logger.info("Iniciando transcricao com modelo: gpt-4o-transcribe")
    texto_transcrito = TranscriptionService().transcrever_audio(
        "gpt-4o-transcribe", caminho_audio
    )
    logger.info("Transcricao concluida (%d caracteres)", len(texto_transcrito or ""))

    caminho_transcricao.parent.mkdir(parents=True, exist_ok=True)
    caminho_transcricao.write_text(texto_transcrito, encoding="utf-8")
    logger.info("Transcricao salva em: %s", caminho_transcricao)

    logger.info("Iniciando geracao dos documentos de escopo")
    scope_service = ProjectScopeService()
    arquivos_escopo, caminho_docx = scope_service.gerar_documentos(texto_transcrito)
    logger.info("Geracao de escopo finalizada (%d arquivos txt)", len(arquivos_escopo))
    logger.info("Documento Word gerado em: %s", caminho_docx)

    print(f"Transcricao salva em: {caminho_transcricao}")
    print("Arquivos de escopo gerados:")
    for arquivo in arquivos_escopo:
        print(f"- {arquivo}")
    print(f"Documento Word gerado: {caminho_docx}")


if __name__ == "__main__":
    main()
