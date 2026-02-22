"""Define a hierarquia de excecoes customizadas da aplicacao."""

class AppError(Exception):
    """Base para excecoes da aplicacao."""


class ConfigurationError(AppError):
    """Erro de configuracao ou variavel de ambiente."""


class MissingAPIKeyError(ConfigurationError):
    """OPENAI_API_KEY ausente."""


class AudioProcessingError(AppError):
    """Erro no processamento de audio."""


class VideoFileNotFoundError(AudioProcessingError):
    """Arquivo de video nao encontrado."""


class FFmpegNotFoundError(AudioProcessingError):
    """Binario ffmpeg indisponivel."""


class AudioExtractionError(AudioProcessingError):
    """Falha ao extrair audio com ffmpeg."""


class ScopeGenerationError(AppError):
    """Erro durante geracao de escopo."""


class PromptDirectoryNotFoundError(ScopeGenerationError):
    """Diretorio de prompts nao encontrado."""


class PromptFileNotFoundError(ScopeGenerationError):
    """Nenhum arquivo de prompt valido encontrado."""


class SectionFileNotFoundError(ScopeGenerationError):
    """Arquivo de secao nao encontrado."""


class DocumentGenerationError(ScopeGenerationError):
    """Erro ao montar documento Word."""


class DependencyNotInstalledError(AppError):
    """Dependencia obrigatoria nao encontrada."""
