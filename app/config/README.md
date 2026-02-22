# app/config

Camada de configuracao de paths e convencoes de organizacao de arquivos.

## Responsabilidades

- Centralizar caminhos padrao da aplicacao.
- Definir convencao de nome para pasta de artefatos processados.
- Evitar strings de path espalhadas pelo codigo.

## Arquivos

- `__init__.py`: exp?e os caminhos e utilitarios de configuracao.
- `paths.py`: define paths padrao da aplicacao e a regra de timestamp.

## Funcao-Chave

- `gerar_pasta_processada(...)`:
  - gera caminho no formato `processada_DD-MM-AAAA_HH-MM-SS`
  - utilizada no arquivamento dos artefatos da execucao
