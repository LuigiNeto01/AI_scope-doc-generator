"""Define caminhos padrao de entrada/saida e convencao de pastas processadas."""

from __future__ import annotations

from datetime import datetime
from pathlib import Path

# Diretorio base para entrada/saida da pipeline.
DATA_DIR = Path("data")

DEFAULT_VIDEO_PATH = DATA_DIR / "Video.mp4"
DEFAULT_AUDIO_DIR = DATA_DIR / "audio"
DEFAULT_TRANSCRIPTION_PATH = DATA_DIR / "transcricao" / "audio_transcrito.txt"
DEFAULT_SCOPE_DIR = DATA_DIR / "escopo"
DEFAULT_SCOPE_DOCX_PATH = DEFAULT_SCOPE_DIR / "documento_escopo.docx"
DEFAULT_SCOPE_NORMALIZED_TXT_PATH = DEFAULT_SCOPE_DIR / "documento_escopo_normalizado.txt"

PROCESSADA_PREFIX = "processada"


def gerar_pasta_processada(base_dir: Path = DATA_DIR, now: datetime | None = None) -> Path:
    """Monta o caminho da pasta de arquivamento no formato processada_DD-MM-AAAA_HH-MM-SS."""
    referencia = now or datetime.now()
    timestamp = referencia.strftime("%d-%m-%Y_%H-%M-%S")
    return base_dir / f"{PROCESSADA_PREFIX}_{timestamp}"
