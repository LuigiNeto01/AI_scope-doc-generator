"""Script de teste para normalizar secoes existentes e gerar TXT+DOCX sem regenerar escopo."""

import argparse
from pathlib import Path
import re
import sys

ROOT_DIR = Path(__file__).resolve().parents[1]
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from app.services.project_scope_service import ProjectScopeService
from app.core.constants import DEFAULT_SCOPE_DIR, DEFAULT_TEXT_MODEL
from app.core.exceptions import ScopeGenerationError


SECAO_RE = re.compile(r"^\d+_.+\.txt$")


def _coletar_arquivos_secao(pasta_escopo: Path) -> list[str]:
    """Coleta apenas arquivos de secao no padrao NN_nome.txt e retorna ordenados."""
    arquivos: list[Path] = []
    for path in pasta_escopo.glob("*.txt"):
        if not path.is_file():
            continue
        if not SECAO_RE.match(path.name):
            continue
        arquivos.append(path)

    def ordem(path: Path) -> tuple[int, str]:
        """Ordena secoes com base no prefixo numerico do nome do arquivo."""
        prefixo = path.name.split("_", 1)[0]
        return (int(prefixo), path.name)

    return [str(path) for path in sorted(arquivos, key=ordem)]


def main() -> None:
    """Executa teste de normalizacao final usando secoes ja existentes no projeto."""
    parser = argparse.ArgumentParser(
        description=(
            "Script de teste para usar os .txt de escopo ja existentes, "
            "normalizar com IA e gerar .txt consolidado + .docx."
        )
    )
    parser.add_argument(
        "--input-dir",
        default=str(DEFAULT_SCOPE_DIR),
        help="Pasta com os arquivos de secao (default: data/escopo)",
    )
    parser.add_argument(
        "--output-docx",
        default="data/escopo/documento_escopo_teste.docx",
        help="Caminho do DOCX de saida (default: data/escopo/documento_escopo_teste.docx)",
    )
    parser.add_argument(
        "--output-txt",
        default="data/escopo/documento_escopo_normalizado_teste.txt",
        help=(
            "Caminho do TXT consolidado normalizado "
            "(default: data/escopo/documento_escopo_normalizado_teste.txt)"
        ),
    )
    parser.add_argument(
        "--model-normalizacao",
        default=DEFAULT_TEXT_MODEL,
        help="Modelo para normalizacao via IA (default: gpt-4o-mini)",
    )
    args = parser.parse_args()

    pasta_escopo = Path(args.input_dir)
    if not pasta_escopo.exists():
        raise ScopeGenerationError(f"Pasta nao encontrada: {pasta_escopo}")

    arquivos_txt = _coletar_arquivos_secao(pasta_escopo)
    if not arquivos_txt:
        raise ScopeGenerationError(
            f"Nenhum arquivo de secao no formato 'NN_nome.txt' encontrado em: {pasta_escopo}"
        )

    # Este script nao gera novas secoes; apenas normaliza e materializa TXT+DOCX.
    service = ProjectScopeService(output_dir=str(pasta_escopo))
    caminho_docx = service.gerar_documento_word_de_txts(
        arquivos_txt=arquivos_txt,
        arquivo_saida=args.output_docx,
        arquivo_texto_normalizado_saida=args.output_txt,
        normalizar_com_ia=True,
        model_normalizacao=args.model_normalizacao,
    )

    print("Arquivos de secao usados:")
    for arquivo in arquivos_txt:
        print(f"- {arquivo}")
    print(f"TXT normalizado gerado: {args.output_txt}")
    print(f"DOCX gerado: {caminho_docx}")


if __name__ == "__main__":
    main()
