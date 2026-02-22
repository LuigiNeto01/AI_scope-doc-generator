"""Orquestra o fluxo completo da pipeline de processamento e geracao de escopo."""

from __future__ import annotations

import logging

from app.config.paths import DEFAULT_AUDIO_DIR, DEFAULT_TRANSCRIPTION_PATH, DEFAULT_VIDEO_PATH
from app.core.constants import DEFAULT_TRANSCRIPTION_MODEL
from app.services import AudioProcessingService, ProjectScopeService
from app.services.ai.transcription_service import TranscriptionService
from app.services.archive_service import ArchiveService

logger = logging.getLogger(__name__)


def run_pipeline() -> None:
    """Orquestra a pipeline completa: extracao, transcricao, escopo e arquivamento."""
    caminho_video = DEFAULT_VIDEO_PATH
    output_dir = str(DEFAULT_AUDIO_DIR)
    caminho_transcricao = DEFAULT_TRANSCRIPTION_PATH

    logger.info("Iniciando pipeline")
    # 1) Extracao de audio do video de entrada.
    logger.info("Extraindo audio do video: %s", caminho_video)
    audio_service = AudioProcessingService(output_dir=output_dir)
    caminho_audio = audio_service.extrair_audio(str(caminho_video))
    logger.info("Audio extraido em: %s", caminho_audio)

    # 2) Transcricao do audio com modelo dedicado.
    logger.info("Iniciando transcricao com modelo: %s", DEFAULT_TRANSCRIPTION_MODEL)
    texto_transcrito = TranscriptionService().transcrever_audio(
        DEFAULT_TRANSCRIPTION_MODEL,
        caminho_audio,
    )
    logger.info("Transcricao concluida (%d caracteres)", len(texto_transcrito or ""))

    caminho_transcricao.parent.mkdir(parents=True, exist_ok=True)
    caminho_transcricao.write_text(texto_transcrito, encoding="utf-8")
    logger.info("Transcricao salva em: %s", caminho_transcricao)

    # 3) Geracao das secoes de escopo + consolidacao final em Word.
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

    # 4) Arquivamento de todos os artefatos para historico da execucao.
    pasta_processada = ArchiveService().arquivar_processados(
        caminho_video=str(caminho_video),
        caminho_audio=caminho_audio,
        caminho_transcricao=caminho_transcricao,
        arquivos_escopo=arquivos_escopo,
    )
    print(f"Arquivos processados movidos para: {pasta_processada}")
