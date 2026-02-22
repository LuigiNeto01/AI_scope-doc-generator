from __future__ import annotations

import os
import shutil
import subprocess
from pathlib import Path


class AudioExtractionService:
    def __init__(self, output_dir: str = "data/audio"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def extrair_audio(self, caminho_video: str, formato_saida: str = "mp3") -> str:
        video_path = Path(caminho_video)
        if not video_path.exists():
            raise FileNotFoundError(f"Video nao encontrado: {video_path}")

        audio_path = self.output_dir / f"{video_path.stem}.{formato_saida}"
        ffmpeg_bin = self._resolver_ffmpeg()

        command = [
            ffmpeg_bin,
            "-y",
            "-i",
            str(video_path),
            "-vn",
            "-acodec",
            "libmp3lame",
            str(audio_path),
        ]

        try:
            subprocess.run(command, check=True, capture_output=True, text=True)
        except FileNotFoundError as exc:
            raise RuntimeError(
                "ffmpeg nao foi encontrado. Instale com 'winget install Gyan.FFmpeg' "
                "ou 'pip install imageio-ffmpeg'."
            ) from exc
        except subprocess.CalledProcessError as exc:
            raise RuntimeError(f"Falha ao extrair audio: {exc.stderr}") from exc

        return str(audio_path)

    @staticmethod
    def _resolver_ffmpeg() -> str:
        env_bin = os.getenv("FFMPEG_BINARY")
        if env_bin:
            return env_bin

        path_bin = shutil.which("ffmpeg")
        if path_bin:
            return path_bin

        try:
            import imageio_ffmpeg

            return imageio_ffmpeg.get_ffmpeg_exe()
        except Exception as exc:
            raise RuntimeError(
                "ffmpeg nao foi encontrado no PATH e fallback via imageio-ffmpeg "
                "nao esta disponivel."
            ) from exc
