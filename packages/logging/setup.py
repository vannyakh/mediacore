"""Central logging setup for MediaCore services."""

from __future__ import annotations

import logging
import sys

from packages.config.settings import get_settings


def setup_logging(level: str | None = None) -> None:
    settings = get_settings()
    log_level = (level or settings.log_level).upper()
    logging.basicConfig(
        level=getattr(logging, log_level, logging.INFO),
        format="%(asctime)s %(levelname)s [%(name)s] %(message)s",
        stream=sys.stdout,
        force=True,
    )


def get_logger(name: str = "mediacore") -> logging.Logger:
    return logging.getLogger(name)
