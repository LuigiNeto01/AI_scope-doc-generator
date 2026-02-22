"""Script utilitario para gerar DOCX de escopo a partir de secoes txt existentes."""

import argparse
from pathlib import Path
import sys

ROOT_DIR = Path(__file__).resolve().parents[1]
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from app.services.project_scope_service import ProjectScopeService
from app.core.constants import DEFAULT_SCOPE_DIR, DEFAULT_SCOPE_DOCX_PATH, DEFAULT_TEXT_MODEL
from app.core.exceptions import ScopeGenerationError


def _coletar_arquivos_txt(pasta_escopo: Path) -> list[str]:
    """Coleta e ordena os arquivos de secao .txt de uma pasta de escopo."""
    arquivos = []
    for path in pasta_escopo.glob("*.txt"):
        if not path.is_file():
            continue
        if path.name.startswith("_"):
            continue
        arquivos.append(path)

    def ordem(path: Path) -> tuple[int, str]:
        """Calcula chave de ordenacao com base no prefixo numerico do nome."""
        nome = path.name
        prefixo = nome.split("_", 1)[0]
        if prefixo.isdigit():
            return (int(prefixo), nome)
        return (10**9, nome)

    return [str(path) for path in sorted(arquivos, key=ordem)]


def main() -> None:
    """Executa a geracao de DOCX usando secoes existentes, com normalizacao opcional."""
    parser = argparse.ArgumentParser(
        description="Gera o DOCX final de escopo usando os .txt ja existentes (sem IA)."
    )
    parser.add_argument(
        "--input-dir",
        default=str(DEFAULT_SCOPE_DIR),
        help="Pasta com os arquivos .txt de secoes (default: data/escopo)",
    )
    parser.add_argument(
        "--output",
        default=str(DEFAULT_SCOPE_DOCX_PATH),
        help="Caminho do DOCX de saida (default: data/escopo/documento_escopo.docx)",
    )
    parser.add_argument(
        "--model-normalizacao",
        default=DEFAULT_TEXT_MODEL,
        help="Modelo para normalizacao via IA (default: gpt-4o-mini)",
    )
    parser.add_argument(
        "--no-normalize-with-ai",
        action="store_true",
        help="Desativa normalizacao via IA antes de montar o DOCX.",
    )
    args = parser.parse_args()

    pasta_escopo = Path(args.input_dir)
    if not pasta_escopo.exists():
        raise ScopeGenerationError(f"Pasta nao encontrada: {pasta_escopo}")

    arquivos_txt = _coletar_arquivos_txt(pasta_escopo)
    if not arquivos_txt:
        raise ScopeGenerationError(f"Nenhum .txt encontrado em: {pasta_escopo}")

    # Reaproveita somente os artefatos existentes para evitar custo de regeneracao completa.
    service = ProjectScopeService(output_dir=str(pasta_escopo))
    caminho_docx = service.gerar_documento_word_de_txts(
        arquivos_txt=arquivos_txt,
        arquivo_saida=args.output,
        normalizar_com_ia=not args.no_normalize_with_ai,
        model_normalizacao=args.model_normalizacao,
    )

    print("Arquivos usados:")
    for arquivo in arquivos_txt:
        print(f"- {arquivo}")
    print(f"DOCX gerado: {caminho_docx}")


if __name__ == "__main__":
    main()
