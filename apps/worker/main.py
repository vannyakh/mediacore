"""Dramatiq worker entrypoint."""

from __future__ import annotations

import logging

from apps.api.db.session import init_db
from apps.worker import actors  # noqa: F401 — register actors
from jobqueue.broker import configure_broker

logging.basicConfig(level=logging.INFO)


def run() -> None:
    configure_broker()
    init_db()
    import subprocess
    import sys

    # Delegate to dramatiq CLI for process management.
    cmd = [sys.executable, "-m", "dramatiq", "apps.worker.actors", "--processes", "1", "--threads", "4"]
    raise SystemExit(subprocess.call(cmd))


if __name__ == "__main__":
    run()
