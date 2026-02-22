# app/services/ai

Subcamada de integracao com modelos da OpenAI.

## Responsabilidades

- Inicializar cliente OpenAI de forma padronizada.
- Encapsular chamadas de transcricao e geracao de texto.
- Centralizar validacao de credenciais de IA.

## Arquivos

- `__init__.py`: marca e exporta o pacote de IA.
- `base_ai.py`: classe base para inicializacao do cliente OpenAI.
- `transcription_service.py`: transcricao de audio para texto.
- `generative_service.py`: geracao de texto a partir de prompts.
