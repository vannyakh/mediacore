"""MediaCore Dramatiq actors."""

from __future__ import annotations

import json
import logging
from datetime import datetime, timezone
from pathlib import Path

import dramatiq
from sqlalchemy import select

from apps.api.db.models import Download, Job, JobStatus
from apps.api.db.session import SessionLocal
from packages.core.exceptions import MediaCoreError, PluginError
from packages.engine.engine import MediaCoreEngine
from packages.events.bus import EventType, get_event_bus
from packages.media.wrapper import (
    FFmpegError,
    convert_media,
    extract_audio,
    extract_thumbnail,
)
from packages.plugins.runtime import ensure_ffmpeg, get_storage
from packages.queue.broker import configure_broker
from packages.storage.base import StorageBackend

configure_broker()
logger = logging.getLogger("mediacore.worker")

try:
    from packages.config.settings import get_settings
    from packages.events.redis_bridge import configure_event_bridge

    _settings = get_settings()
    if _settings.events_redis_enabled:
        configure_event_bridge(get_event_bus(), _settings.redis_url, subscribe=False)
except Exception:  # noqa: BLE001
    logger.debug("Worker event Redis publisher not attached", exc_info=True)


def _fail(job: Job, db, message: str) -> None:
    job.status = JobStatus.failed
    job.error = message
    db.add(job)
    db.commit()
    get_event_bus().emit(EventType.FAILED, job_id=job.id, error=message)


def _is_cancelled(db, job_id: str) -> bool:
    job = db.scalar(select(Job).where(Job.id == job_id))
    return job is not None and job.status == JobStatus.cancelled


def _process_download(job_id: str) -> None:
    storage = get_storage()
    engine = MediaCoreEngine()

    with SessionLocal() as db:
        job = db.scalar(select(Job).where(Job.id == job_id))
        if job is None:
            return
        if job.status == JobStatus.cancelled:
            return
        job.status = JobStatus.running
        db.add(job)
        db.commit()
        try:
            dest = storage.job_dir(job.id) / "media"
            result = engine.download(
                job.url,
                job.format_id or "original",
                dest,
                job_id=job.id,
            )
            # Re-check cancel after long download
            db.refresh(job)
            if job.status == JobStatus.cancelled:
                return
            public = storage.publish(job.id, result.path)
            db.add(
                Download(
                    job_id=job.id,
                    path=str(result.path),
                    format_id=result.format_id,
                    container=result.container,
                    filesize=result.filesize,
                    content_type=result.content_type,
                )
            )
            job.status = JobStatus.completed
            job.result_path = str(result.path)
            job.result_url = public
            job.completed_at = datetime.now(timezone.utc)
            job.error = None
            db.add(job)
            db.commit()
        except MediaCoreError as exc:
            if _is_cancelled(db, job_id):
                return
            _fail(job, db, exc.message)
        except Exception as exc:  # noqa: BLE001
            if _is_cancelled(db, job_id):
                return
            logger.exception("download failed")
            _fail(job, db, str(exc))


def _ensure_source(job: Job, storage: StorageBackend) -> Path:
    """Download remote URL first when needed, else use local path."""
    url = job.url
    if url.startswith("file://") or Path(url).exists():
        path = Path(url.removeprefix("file://")) if url.startswith("file://") else Path(url)
        return path

    engine = MediaCoreEngine()
    dest = storage.job_dir(job.id) / "source"
    result = engine.download(url, job.format_id or "original", dest, job_id=job.id)
    return result.path


def _process_media_op(job_id: str, operation: str) -> None:
    storage = get_storage()
    with SessionLocal() as db:
        job = db.scalar(select(Job).where(Job.id == job_id))
        if job is None:
            return
        if job.status == JobStatus.cancelled:
            return
        job.status = JobStatus.running
        db.add(job)
        db.commit()
        get_event_bus().emit(EventType.PROCESSING_STARTED, job_id=job.id, operation=operation)

        try:
            if operation == "subtitles":
                engine = MediaCoreEngine()
                subs = engine.subtitles(job.url)
                payload = [s.to_dict() if hasattr(s, "to_dict") else s for s in subs]
                out = storage.job_dir(job.id) / "subtitles.json"
                out.write_text(json.dumps(payload, indent=2), encoding="utf-8")
                job.result_path = str(out)
                job.result_url = storage.publish(job.id, out)
                job.status = JobStatus.completed
                job.completed_at = datetime.now(timezone.utc)
                db.add(job)
                db.commit()
                get_event_bus().emit(EventType.COMPLETED, job_id=job.id, operation=operation)
                return

            if operation == "video":
                # Alias for download of best/original video
                _process_download(job_id)
                return

            if operation in {"audio", "thumbnail", "convert", "clip"}:
                ensure_ffmpeg()

            source = _ensure_source(job, storage)
            dest_dir = storage.job_dir(job.id)

            if operation == "audio":
                dest = dest_dir / "audio.mp3"
                extract_audio(source, dest)
            elif operation == "thumbnail":
                dest = dest_dir / "thumbnail.jpg"
                # Prefer provider thumbnail URL metadata when available
                thumb = MediaCoreEngine().thumbnail(job.url)
                thumb_url = thumb.url if thumb is not None else None
                if thumb_url and thumb_url.startswith("http"):
                    from packages.core.downloader import download_file

                    download_file(thumb_url, dest)
                else:
                    extract_thumbnail(source, dest)
            elif operation == "convert":
                options = {}
                if job.meta_json:
                    options = json.loads(job.meta_json).get("options") or {}
                ext = options.get("container", "mp4")
                dest = dest_dir / f"converted.{ext}"
                convert_media(source, dest)
            elif operation == "clip":
                options = {}
                if job.meta_json:
                    options = json.loads(job.meta_json).get("options") or {}
                start = str(options.get("start", 0))
                duration = str(options.get("duration", 10))
                dest = dest_dir / "clip.mp4"
                import subprocess

                cmd = [
                    "ffmpeg",
                    "-y",
                    "-ss",
                    start,
                    "-i",
                    str(source),
                    "-t",
                    duration,
                    str(dest),
                ]
                result = subprocess.run(cmd, capture_output=True, text=True)
                if result.returncode != 0:
                    raise FFmpegError(result.stderr.strip() or "clip failed")
            else:
                raise MediaCoreError(f"Unknown operation: {operation}", code="unknown_operation")

            job.result_path = str(dest)
            job.result_url = storage.publish(job.id, dest)
            job.status = JobStatus.completed
            job.completed_at = datetime.now(timezone.utc)
            job.error = None
            db.add(job)
            db.commit()
            get_event_bus().emit(EventType.COMPLETED, job_id=job.id, operation=operation)
        except (MediaCoreError, PluginError, FFmpegError) as exc:
            message = getattr(exc, "message", str(exc))
            _fail(job, db, message)
        except Exception as exc:  # noqa: BLE001
            logger.exception("process failed")
            _fail(job, db, str(exc))


@dramatiq.actor(queue_name="download", max_retries=3)
def download_job(job_id: str) -> None:
    _process_download(job_id)


@dramatiq.actor(queue_name="analyze", max_retries=2)
def analyze_job(job_id: str) -> None:
    engine = MediaCoreEngine()
    with SessionLocal() as db:
        job = db.scalar(select(Job).where(Job.id == job_id))
        if job is None:
            return
        if job.status == JobStatus.cancelled:
            return
        job.status = JobStatus.running
        db.add(job)
        db.commit()
        try:
            meta = engine.analyze(job.url, job_id=job.id)
            job.meta_json = json.dumps(meta.to_dict())
            job.platform = meta.platform
            job.status = JobStatus.completed
            job.completed_at = datetime.now(timezone.utc)
            db.add(job)
            db.commit()
            get_event_bus().emit(EventType.COMPLETED, job_id=job.id, operation="analyze")
        except MediaCoreError as exc:
            _fail(job, db, exc.message)


@dramatiq.actor(queue_name="cleanup", max_retries=1)
def cleanup_job(job_id: str) -> None:
    storage = get_storage()
    with SessionLocal() as db:
        job = db.scalar(select(Job).where(Job.id == job_id))
        if job is None:
            return
        storage.delete_job(job_id)
        job.status = JobStatus.expired
        job.result_path = None
        job.result_url = None
        db.add(job)
        db.commit()


@dramatiq.actor(queue_name="retry", max_retries=2)
def process_job(job_id: str, operation: str) -> None:
    _process_media_op(job_id, operation)


def run_download_sync(job_id: str) -> None:
    _process_download(job_id)


def run_process_sync(job_id: str, operation: str) -> None:
    _process_media_op(job_id, operation)
