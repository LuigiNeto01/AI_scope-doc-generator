# app/services

Arquivos desta pasta:

- udio_extraction_service.py: extrai audio de video com fmpeg, com fallback para imageio-ffmpeg quando necessario.
- udio_processing_service.py: facade simples para o fluxo de extracao de audio.
- project_scope_service.py: orquestra leitura dos prompts, geracao das secoes por IA, normalizacao final e montagem do documento .docx.

Subpasta relevante:

- i/: camada de acesso aos modelos da OpenAI (transcricao e geracao).

