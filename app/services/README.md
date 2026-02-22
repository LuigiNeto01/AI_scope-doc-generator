# app/services

Camada de servicos de dominio da aplicacao.

## Responsabilidades

- Implementar regras operacionais da pipeline.
- Isolar integracoes externas (ffmpeg, OpenAI, python-docx).
- Materializar artefatos de saida (txt/docx/arquivamento).

## Arquivos

- `audio_extraction_service.py`: extrai audio de video com `ffmpeg`.
- `audio_processing_service.py`: facade simples para processamento de audio.
- `project_scope_service.py`: gera secoes, normaliza texto e monta DOCX final.
- `archive_service.py`: move artefatos processados para pasta versionada por timestamp.
- `__init__.py`: exporta servicos principais da camada.

## Subpasta

- `ai/`: servicos de IA (transcricao e geracao textual).
