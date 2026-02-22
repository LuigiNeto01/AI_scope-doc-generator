# app/pipeline

Camada de orquestracao de alto nivel da aplicacao.

## Responsabilidades

- Encadear as etapas da pipeline em ordem correta.
- Integrar servicos de audio, IA, escopo e arquivamento.
- Manter o ponto de entrada (`main.py`) enxuto.

## Arquivos

- `run_pipeline.py`: executa o fluxo completo da pipeline.
- `__init__.py`: exporta `run_pipeline`.
