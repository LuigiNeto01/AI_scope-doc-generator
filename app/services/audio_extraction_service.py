"""Servico de extracao de audio de video com ffmpeg e tratamentos de fallback."""

from __future__ import annotations

import os
import shutil
import subprocess
from pathlib import Path

from app.core.constants import (
    DEFAULT_AUDIO_CODEC,
    DEFAULT_AUDIO_DIR,
    DEFAULT_AUDIO_FORMAT,
    FFMPEG_BINARY_ENV,
)
from app.core.exceptions import (
    AudioExtractionError,
    FFmpegNotFoundError,
    VideoFileNotFoundError,
)


class AudioExtractionService:
    """Extrai trilha de audio de um video usando ffmpeg."""

    def __init__(self, output_dir: str = str(DEFAULT_AUDIO_DIR)):
        """Inicializa o diretorio de saida do audio extraido."""
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def extrair_audio(
        self,
        caminho_video: str,
        formato_saida: str = DEFAULT_AUDIO_FORMAT,
    ) -> str:
        """Extrai o audio do video informado e retorna o caminho do arquivo gerado."""
        video_path = Path(caminho_video)
        if not video_path.exists():
            raise VideoFileNotFoundError(f"Video nao encontrado: {video_path}")

        audio_path = self.output_dir / f"{video_path.stem}.{formato_saida}"
        ffmpeg_bin = self._resolver_ffmpeg()

        # Comando ffmpeg minimo para:
        # - sobrescrever arquivo existente (-y)
        # - ler video de entrada (-i)
        # - remover stream de video (-vn)
        # - forcar codec de audio desejado
        command = [
            ffmpeg_bin,
            "-y",
            "-i",
            str(video_path),
            "-vn",
            "-acodec",
            DEFAULT_AUDIO_CODEC,
            str(audio_path),
        ]

        try:
            # capture_output=True facilita diagnostico quando o ffmpeg falha.
            subprocess.run(command, check=True, capture_output=True, text=True)
        except FileNotFoundError as exc:
            raise FFmpegNotFoundError(
                "ffmpeg nao foi encontrado. Instale com 'winget install Gyan.FFmpeg' "
                "ou 'pip install imageio-ffmpeg'."
            ) from exc
        except subprocess.CalledProcessError as exc:
            # stderr do ffmpeg costuma trazer diagnostico preciso (codec, permissao, arquivo).
            raise AudioExtractionError(f"Falha ao extrair audio: {exc.stderr}") from exc

        return str(audio_path)

    @staticmethod
    def _resolver_ffmpeg() -> str:
        """Resolve o executavel do ffmpeg via env, PATH ou fallback imageio-ffmpeg."""
        # Prioridade 1: variavel de ambiente explicita (controle total em ambientes CI/CD).
        env_bin = os.getenv(FFMPEG_BINARY_ENV)
        if env_bin:
            return env_bin

        # Prioridade 2: binario no PATH do sistema.
        path_bin = shutil.which("ffmpeg")
        if path_bin:
            return path_bin

        try:
            import imageio_ffmpeg

            # Prioridade 3: fallback gerenciado pela dependencia Python.
            return imageio_ffmpeg.get_ffmpeg_exe()
        except Exception as exc:
            raise FFmpegNotFoundError(
                "ffmpeg nao foi encontrado no PATH e fallback via imageio-ffmpeg "
                "nao esta disponivel."
            ) from exc
