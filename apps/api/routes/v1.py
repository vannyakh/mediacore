"""MediaCore REST API v1."""

from __future__ import annotations

import json

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from apps.api.config import get_settings
from apps.api.db.models import ApiKey, Job, JobStatus
from apps.api.db.session import get_db
from apps.api.middleware.auth import require_api_key
from apps.api.schemas import (
    AnalyzeRequest,
    AnalyzeResponse,
    DownloadRequest,
    FormatOut,
    JobCreateResponse,
    JobResponse,
    MediaOpRequest,
    PluginOut,
    ProviderOut,
    SystemOut,
)
from packages.core.exceptions import MediaCoreError
from packages.engine.engine import MediaCoreEngine
from packages.events.bus import EventType, get_event_bus
from packages.media.wrapper import ffmpeg_available
from packages.plugins.loader import get_plugin_loader
from packages.queue.broker import enqueue_download, enqueue_process

router = APIRouter(prefix="/v1", tags=["v1"])


def _engine() -> MediaCoreEngine:
    return MediaCoreEngine()


def _http_error(exc: MediaCoreError) -> HTTPException:
    return HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail={"error": exc.message, "code": exc.code},
    )


def _create_job(
    db: Session,
    api_key: ApiKey,
    *,
    job_type: str,
    url: str,
    format_id: str | None = None,
    platform: str | None = None,
    meta: dict | None = None,
) -> Job:
    job = Job(
        user_id=api_key.user_id,
        api_key_id=api_key.id,
        type=job_type,
        status=JobStatus.queued,
        url=url,
        platform=platform,
        format_id=format_id,
        meta_json=json.dumps(meta) if meta else None,
    )
    db.add(job)
    db.commit()
    db.refresh(job)
    get_event_bus().emit(EventType.JOB_CREATED, job_id=job.id, type=job_type, url=url)
    return job


@router.post("/analyze", response_model=AnalyzeResponse)
def analyze(body: AnalyzeRequest, _: ApiKey = Depends(require_api_key)) -> AnalyzeResponse:
    settings = get_settings()
    try:
        meta = _engine().analyze(body.url, allow_private=settings.allow_private_urls)
    except MediaCoreError as exc:
        raise _http_error(exc) from exc
    return AnalyzeResponse(
        platform=meta.platform,
        title=meta.title,
        duration=meta.duration,
        thumbnail=meta.thumbnail,
        description=meta.description,
        author=meta.author,
        url=meta.url,
        manifest=meta.manifest,
        formats=[FormatOut(**f.to_dict()) for f in meta.formats],
    )


@router.post(
    "/download",
    response_model=JobCreateResponse,
    status_code=status.HTTP_202_ACCEPTED,
)
def download(
    body: DownloadRequest,
    api_key: ApiKey = Depends(require_api_key),
    db: Session = Depends(get_db),
) -> JobCreateResponse:
    settings = get_settings()
    try:
        meta = _engine().analyze(body.url, allow_private=settings.allow_private_urls)
    except MediaCoreError as exc:
        raise _http_error(exc) from exc
    job = _create_job(
        db,
        api_key,
        job_type="download",
        url=body.url,
        format_id=body.format,
        platform=meta.platform,
        meta=meta.to_dict(),
    )
    enqueue_download(job.id)
    return JobCreateResponse(job_id=job.id, status=job.status.value, type=job.type)


def _enqueue_media_op(
    body: MediaOpRequest,
    api_key: ApiKey,
    db: Session,
    operation: str,
) -> JobCreateResponse:
    target = body.url or body.path
    if not target:
        raise HTTPException(status_code=400, detail="url or path is required")
    job = _create_job(
        db,
        api_key,
        job_type=operation,
        url=target,
        format_id=body.format,
        meta={"options": body.options, "operation": operation},
    )
    enqueue_process(job.id, operation)
    return JobCreateResponse(job_id=job.id, status=job.status.value, type=job.type)


@router.post("/audio", response_model=JobCreateResponse, status_code=202)
def audio(
    body: MediaOpRequest,
    api_key: ApiKey = Depends(require_api_key),
    db: Session = Depends(get_db),
) -> JobCreateResponse:
    return _enqueue_media_op(body, api_key, db, "audio")


@router.post("/video", response_model=JobCreateResponse, status_code=202)
def video(
    body: MediaOpRequest,
    api_key: ApiKey = Depends(require_api_key),
    db: Session = Depends(get_db),
) -> JobCreateResponse:
    return _enqueue_media_op(body, api_key, db, "video")


@router.post("/subtitles", response_model=JobCreateResponse, status_code=202)
def subtitles(
    body: MediaOpRequest,
    api_key: ApiKey = Depends(require_api_key),
    db: Session = Depends(get_db),
) -> JobCreateResponse:
    return _enqueue_media_op(body, api_key, db, "subtitles")


@router.post("/thumbnail", response_model=JobCreateResponse, status_code=202)
def thumbnail(
    body: MediaOpRequest,
    api_key: ApiKey = Depends(require_api_key),
    db: Session = Depends(get_db),
) -> JobCreateResponse:
    return _enqueue_media_op(body, api_key, db, "thumbnail")


@router.post("/convert", response_model=JobCreateResponse, status_code=202)
def convert(
    body: MediaOpRequest,
    api_key: ApiKey = Depends(require_api_key),
    db: Session = Depends(get_db),
) -> JobCreateResponse:
    return _enqueue_media_op(body, api_key, db, "convert")


@router.post("/clip", response_model=JobCreateResponse, status_code=202)
def clip(
    body: MediaOpRequest,
    api_key: ApiKey = Depends(require_api_key),
    db: Session = Depends(get_db),
) -> JobCreateResponse:
    return _enqueue_media_op(body, api_key, db, "clip")


@router.post("/jobs", response_model=JobCreateResponse, status_code=202)
def create_job(
    body: DownloadRequest,
    api_key: ApiKey = Depends(require_api_key),
    db: Session = Depends(get_db),
) -> JobCreateResponse:
    """Generic job create — currently aliases download."""
    return download(body, api_key, db)


@router.get("/jobs/{job_id}", response_model=JobResponse)
def get_job(
    job_id: str,
    _: ApiKey = Depends(require_api_key),
    db: Session = Depends(get_db),
) -> JobResponse:
    job = db.scalar(select(Job).where(Job.id == job_id))
    if job is None:
        raise HTTPException(status_code=404, detail="Job not found")
    return JobResponse(
        id=job.id,
        status=job.status.value,
        type=job.type,
        url=job.url,
        platform=job.platform,
        format_id=job.format_id,
        error=job.error,
        result_url=job.result_url,
        created_at=job.created_at,
        completed_at=job.completed_at,
    )


@router.get("/providers", response_model=list[ProviderOut])
def list_providers(_: ApiKey = Depends(require_api_key)) -> list[ProviderOut]:
    return [ProviderOut(**p) for p in _engine().providers()]


@router.get("/plugins", response_model=list[PluginOut])
def list_plugins(_: ApiKey = Depends(require_api_key)) -> list[PluginOut]:
    plugins = get_plugin_loader().list()
    return [PluginOut(**p.to_dict()) for p in plugins]


@router.get("/system", response_model=SystemOut)
def system(_: ApiKey = Depends(require_api_key)) -> SystemOut:
    settings = get_settings()
    from mediacore import __version__

    return SystemOut(
        name=settings.app_name,
        version=__version__,
        environment=settings.environment,
        providers=len(_engine().providers()),
        plugins=len(get_plugin_loader().list()),
        ffmpeg=ffmpeg_available(),
        events_retained=len(get_event_bus().history(1000)),
    )
