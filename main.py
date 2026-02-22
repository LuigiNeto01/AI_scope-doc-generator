"""Ponto de entrada da aplicacao; delega a execucao para a camada de pipeline."""

import logging

from app.core.exceptions import AppError
from app.pipeline import run_pipeline

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
)
logger = logging.getLogger(__name__)


def main() -> None:
    """Executa o ponto de entrada da aplicacao com tratamento de erro padronizado."""
    try:
        # A orquestracao foi movida para a camada de pipeline para manter o main enxuto.
        run_pipeline()
    except AppError as exc:
        logger.exception("Falha na pipeline: %s", exc)
        raise SystemExit(1) from exc


if __name__ == "__main__":
    main()
