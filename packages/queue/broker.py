"""Dramatiq broker configuration and enqueue helpers."""

from __future__ import annotations

import logging
import os

import dramatiq
from dramatiq.brokers.redis import RedisBroker
from dramatiq.brokers.stub import StubBroker

logger = logging.getLogger("mediacore.queue")

_broker_configured = False


def configure_broker() -> None:
    global _broker_configured
    if _broker_configured:
        return

    redis_url = os.getenv("REDIS_URL", "redis://localhost:6379/0")
    use_stub = os.getenv("DRAMATIQ_STUB", "").lower() in {"1", "true", "yes"}

    if use_stub:
        broker = StubBroker()
        broker.emit_after("process_boot")
        logger.info("Using Dramatiq StubBroker")
    else:
        broker = RedisBroker(url=redis_url)
        logger.info("Using Redis broker at %s", redis_url)

    dramatiq.set_broker(broker)
    _broker_configured = True


configure_broker()


def enqueue_download(job_id: str) -> None:
    from apps.worker.actors import download_job, run_download_sync

    use_stub = os.getenv("DRAMATIQ_STUB", "").lower() in {"1", "true", "yes"}
    sync_mode = os.getenv("SYNC_DOWNLOAD", "").lower() in {"1", "true", "yes"}
    if use_stub or sync_mode:
        run_download_sync(job_id)
        return
    try:
        download_job.send(job_id)
    except Exception:  # noqa: BLE001
        logger.exception("Failed to enqueue job %s; running synchronously", job_id)
        run_download_sync(job_id)


def enqueue_cleanup(job_id: str) -> None:
    from apps.worker.actors import cleanup_job

    cleanup_job.send(job_id)


def enqueue_analyze(job_id: str) -> None:
    from apps.worker.actors import analyze_job

    analyze_job.send(job_id)


def enqueue_process(job_id: str, operation: str) -> None:
    from apps.worker.actors import process_job

    sync_mode = os.getenv("SYNC_DOWNLOAD", "").lower() in {"1", "true", "yes"}
    use_stub = os.getenv("DRAMATIQ_STUB", "").lower() in {"1", "true", "yes"}
    if use_stub or sync_mode:
        from apps.worker.actors import run_process_sync

        run_process_sync(job_id, operation)
        return
    process_job.send(job_id, operation)
