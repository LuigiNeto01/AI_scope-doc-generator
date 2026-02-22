"""Concentra constantes globais usadas por servicos, scripts e pipeline."""

from pathlib import Path

from app.config.paths import (
    DATA_DIR,
    DEFAULT_AUDIO_DIR,
    DEFAULT_SCOPE_DIR,
    DEFAULT_SCOPE_DOCX_PATH,
    DEFAULT_SCOPE_NORMALIZED_TXT_PATH,
    DEFAULT_TRANSCRIPTION_PATH,
    DEFAULT_VIDEO_PATH,
)

# Ambiente
OPENAI_API_KEY_ENV = "OPENAI_API_KEY"
FFMPEG_BINARY_ENV = "FFMPEG_BINARY"

# Modelos
DEFAULT_TRANSCRIPTION_MODEL = "gpt-4o-transcribe"
DEFAULT_TEXT_MODEL = "gpt-4o-mini"
DEFAULT_SYSTEM_PROMPT = "Voce e um assistente tecnico especializado."

# Paths
DEFAULT_PROMPTS_DIR = Path("app/repositories/prompts")
DEFAULT_WORD_TEMPLATE_PATH = Path("app/repositories/modelo/Modelo.docx")
DEFAULT_WORD_NORMALIZATION_PROMPT_PATH = (
    DEFAULT_PROMPTS_DIR / "_prompt_normalizacao_word.txt"
)

# Audio
DEFAULT_AUDIO_FORMAT = "mp3"
DEFAULT_AUDIO_CODEC = "libmp3lame"
