# scripts

Scripts utilitarios para reprocessamento de artefatos sem executar toda a pipeline.

## Responsabilidades

- Permitir geracao de DOCX a partir de secoes ja existentes.
- Permitir teste de normalizacao final com saida em TXT e DOCX.

## Arquivos

- `gerar_docx_escopo.py`: gera DOCX usando `.txt` existentes, com normalizacao opcional.
- `teste_normalizacao_existentes.py`: normaliza secoes existentes e gera `TXT` consolidado + `DOCX`.

## Quando usar

- Ajustes de prompt/formatacao sem necessidade de nova transcricao.
- Iteracao rapida no layout final do documento.
