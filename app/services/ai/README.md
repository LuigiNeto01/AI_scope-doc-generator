# app/services/ai

Arquivos desta pasta:

- __init__.py: marca o pacote de servicos de IA.
- ase_ai.py: classe base que carrega .env, resolve OPENAI_API_KEY e cria cliente OpenAI para chamadas de modelo.
- 	ranscription_service.py: servico de transcricao de audio usando client.audio.transcriptions.create.
- generative_service.py: servico de geracao textual via chat completions, usado para construir secoes do escopo e normalizar texto.

