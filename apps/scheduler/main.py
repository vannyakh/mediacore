"""Periodic cleanup scheduler."""

from __future__ import annotations

import time

from apps.api.db.session import init_db
from packages.logging.setup import get_logger, setup_logging
from packages.scheduler.cleanup import cleanup_expired_jobs

setup_logging()
logger = get_logger("mediacore.scheduler")


def run(interval_seconds: int = 300) -> None:
    init_db()
    logger.info("Scheduler started (interval=%ss)", interval_seconds)
    while True:
        try:
            n = cleanup_expired_jobs()
            if n:
                logger.info("Enqueued cleanup for %s jobs", n)
        except Exception:  # noqa: BLE001
            logger.exception("Scheduler loop error")
        time.sleep(interval_seconds)


if __name__ == "__main__":
    run()
