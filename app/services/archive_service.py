"""Servico de arquivamento dos artefatos processados ao final de cada execucao."""

from __future__ import annotations

import logging
import shutil
from pathlib import Path

from app.config.paths import DATA_DIR, DEFAULT_SCOPE_DIR, gerar_pasta_processada

logger = logging.getLogger(__name__)


class ArchiveService:
    """Centraliza o arquivamento dos artefatos processados da pipeline."""

    def __init__(
        self,
        data_dir: Path = DATA_DIR,
        scope_dir: Path = DEFAULT_SCOPE_DIR,
    ) -> None:
        """Inicializa caminhos base usados no processo de arquivamento."""
        self.data_dir = data_dir
        self.scope_dir = scope_dir

    def arquivar_processados(
        self,
        caminho_video: str,
        caminho_audio: str,
        caminho_transcricao: Path,
        arquivos_escopo: list[str],
    ) -> Path:
        """Move os artefatos da execucao atual para uma pasta processada com timestamp."""
        pasta_processada = gerar_pasta_processada(base_dir=self.data_dir)
        pasta_processada.mkdir(parents=True, exist_ok=True)

        video_path = Path(caminho_video)
        audio_path = Path(caminho_audio)
        transcricao_path = Path(caminho_transcricao)

        self._mover_arquivo_se_existir(video_path, pasta_processada / "video" / video_path.name)
        self._mover_arquivo_se_existir(audio_path, pasta_processada / "audio" / audio_path.name)
        self._mover_arquivo_se_existir(
            transcricao_path,
            pasta_processada / "transcricao" / transcricao_path.name,
        )

        # Arquivos retornados pela geracao (secoes txt) sao movidos explicitamente.
        for arquivo in arquivos_escopo:
            path = Path(arquivo)
            self._mover_arquivo_se_existir(path, pasta_processada / "escopo" / path.name)

        # Inclui artefatos adicionais do escopo que nao vieram explicitamente na lista.
        if self.scope_dir.exists():
            for path in self.scope_dir.glob("*"):
                if path.is_file():
                    self._mover_arquivo_se_existir(path, pasta_processada / "escopo" / path.name)

        return pasta_processada

    @staticmethod
    def _mover_arquivo_se_existir(origem: Path, destino: Path) -> None:
        """Move um arquivo se ele existir, mantendo logs para rastreabilidade."""
        if not origem.exists():
            logger.warning("Arquivo nao encontrado para arquivamento: %s", origem)
            return
        # Garante que a estrutura de destino exista antes do move.
        destino.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(str(origem), str(destino))
        logger.info("Arquivo movido para processamento: %s", destino)
