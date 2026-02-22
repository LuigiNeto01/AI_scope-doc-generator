import argparse
from pathlib import Path
import sys

ROOT_DIR = Path(__file__).resolve().parents[1]
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from app.services.project_scope_service import ProjectScopeService


def _coletar_arquivos_txt(pasta_escopo: Path) -> list[str]:
    arquivos = []
    for path in pasta_escopo.glob("*.txt"):
        if not path.is_file():
            continue
        if path.name.startswith("_"):
            continue
        arquivos.append(path)

    def ordem(path: Path) -> tuple[int, str]:
        nome = path.name
        prefixo = nome.split("_", 1)[0]
        if prefixo.isdigit():
            return (int(prefixo), nome)
        return (10**9, nome)

    return [str(path) for path in sorted(arquivos, key=ordem)]


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Gera o DOCX final de escopo usando os .txt ja existentes (sem IA)."
    )
    parser.add_argument(
        "--input-dir",
        default="data/escopo",
        help="Pasta com os arquivos .txt de secoes (default: data/escopo)",
    )
    parser.add_argument(
        "--output",
        default="data/escopo/documento_escopo.docx",
        help="Caminho do DOCX de saida (default: data/escopo/documento_escopo.docx)",
    )
    parser.add_argument(
        "--model-normalizacao",
        default="gpt-4o-mini",
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
        raise FileNotFoundError(f"Pasta nao encontrada: {pasta_escopo}")

    arquivos_txt = _coletar_arquivos_txt(pasta_escopo)
    if not arquivos_txt:
        raise FileNotFoundError(f"Nenhum .txt encontrado em: {pasta_escopo}")

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
