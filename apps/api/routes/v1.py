"""MediaCore REST API v1."""

from __future__ import annotations

import asyncio
import json
import queue
from collections.abc import AsyncIterator

from fastapi import APIRouter, Depends, HTTPException, Query, Request, status
from fastapi.responses import StreamingResponse
from sqlalchemy import select
from sqlalchemy.orm import Session

from apps.api.config import get_settings
from apps.api.db.models import ApiKey, Job, JobStatus
from apps.api.db.session import get_db
from apps.api.middleware.auth import require_api_key
from apps.api.schemas import (
    AnalyzeRequest,
    AnalyzeResponse,
    CatalogExtractorOut,
    CatalogSummaryOut,
    DownloadRequest,
    EventOut,
    EventsListOut,
    FormatOut,
    JobCreateResponse,
    JobResponse,
    LiveRequest,
    LiveResponse,
    MediaOpRequest,
    PluginOut,
    ProviderOut,
    SystemOut,
)
from packages.core.exceptions import MediaCoreError
from packages.engine.engine import MediaCoreEngine
from packages.events.bus import Event, EventType, get_event_bus
from packages.events.plugins import plugin_runtime_status
from packages.media.wrapper import ffmpeg_available
from packages.plugins.loader import get_plugin_loader
from packages.plugins.runtime import FFMPEG_PLUGIN
from packages.queue.broker import enqueue_download, enqueue_process

router = APIRouter(prefix="/v1", tags=["v1"])


def _engine() -> MediaCoreEngine:
    return MediaCoreEngine()


def _ffmpeg_ready() -> bool:
    plugin = get_plugin_loader().get(FFMPEG_PLUGIN)
    return bool(ffmpeg_available() and plugin is not None and plugin.status == "available")


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
    manifest = meta.manifest
    if hasattr(manifest, "to_dict"):
        manifest = manifest.to_dict()
    return AnalyzeResponse(
        platform=meta.platform,
        title=meta.title,
        duration=meta.duration,
        thumbnail=meta.thumbnail,
        description=meta.description,
        author=meta.author,
        url=meta.url,
        manifest=manifest,
        is_live=meta.is_live,
        subtitles=[s.to_dict() for s in meta.subtitles],
        formats=[FormatOut.model_validate(f.to_dict()) for f in meta.formats],
    )


@router.post("/live", response_model=LiveResponse)
def live(body: LiveRequest, _: ApiKey = Depends(require_api_key)) -> LiveResponse:
    settings = get_settings()
    try:
        info = _engine().live(body.url, allow_private=settings.allow_private_urls)
    except MediaCoreError as exc:
        raise _http_error(exc) from exc
    if info is None:
        return LiveResponse(is_live=False, status="unsupported")
    return LiveResponse(**info.to_dict())


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


def _job_response(job: Job) -> JobResponse:
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


@router.get("/jobs", response_model=list[JobResponse])
def list_jobs(
    api_key: ApiKey = Depends(require_api_key),
    db: Session = Depends(get_db),
    limit: int = 50,
) -> list[JobResponse]:
    limit = max(1, min(limit, 200))
    q = select(Job)
    if api_key.user_id:
        q = q.where(Job.user_id == api_key.user_id)
    else:
        q = q.where(Job.api_key_id == api_key.id)
    q = q.order_by(Job.created_at.desc()).limit(limit)
    jobs = db.scalars(q).all()
    return [_job_response(j) for j in jobs]


@router.get("/jobs/{job_id}", response_model=JobResponse)
def get_job(
    job_id: str,
    _: ApiKey = Depends(require_api_key),
    db: Session = Depends(get_db),
) -> JobResponse:
    job = db.scalar(select(Job).where(Job.id == job_id))
    if job is None:
        raise HTTPException(status_code=404, detail="Job not found")
    return _job_response(job)


@router.post("/jobs/{job_id}/cancel", response_model=JobResponse)
def cancel_job(
    job_id: str,
    _: ApiKey = Depends(require_api_key),
    db: Session = Depends(get_db),
) -> JobResponse:
    job = db.scalar(select(Job).where(Job.id == job_id))
    if job is None:
        raise HTTPException(status_code=404, detail="Job not found")
    if job.status in {
        JobStatus.completed,
        JobStatus.failed,
        JobStatus.cancelled,
        JobStatus.expired,
    }:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Job already {job.status.value}",
        )
    job.status = JobStatus.cancelled
    job.error = None
    db.add(job)
    db.commit()
    db.refresh(job)
    get_event_bus().emit(EventType.CANCELLED, job_id=job.id, type=job.type, url=job.url)
    return _job_response(job)


@router.get("/events", response_model=EventsListOut)
def list_events(
    _: ApiKey = Depends(require_api_key),
    limit: int = Query(default=50, ge=1, le=500),
    job_id: str | None = None,
) -> EventsListOut:
    events = get_event_bus().history(limit, job_id=job_id)
    return EventsListOut(
        events=[EventOut(**e) for e in events],
        count=len(events),
    )


@router.get("/events/stream")
async def stream_events(
    request: Request,
    _: ApiKey = Depends(require_api_key),
    job_id: str | None = None,
    replay_only: bool = False,
) -> StreamingResponse:
    bus = get_event_bus()
    q: queue.Queue[dict | None] = queue.Queue()

    def _listener(event: Event) -> None:
        if job_id is not None and event.payload.get("job_id") != job_id:
            return
        q.put(event.to_dict())

    bus.on(None, _listener)

    async def _generate() -> AsyncIterator[str]:
        try:
            # Replay recent history first
            for item in bus.history(50, job_id=job_id):
                yield f"event: {item['type']}\ndata: {json.dumps(item)}\n\n"
            if replay_only:
                return
            while True:
                if await request.is_disconnected():
                    break
                try:
                    item = await asyncio.to_thread(q.get, True, 1.0)
                except queue.Empty:
                    yield ": heartbeat\n\n"
                    continue
                if item is None:
                    break
                yield f"event: {item['type']}\ndata: {json.dumps(item)}\n\n"
        finally:
            bus.off(None, _listener)

    return StreamingResponse(
        _generate(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "X-Accel-Buffering": "no",
        },
    )


@router.get("/providers", response_model=list[ProviderOut])
def list_providers(_: ApiKey = Depends(require_api_key)) -> list[ProviderOut]:
    return [ProviderOut(**p) for p in _engine().providers()]


@router.get("/providers/catalog", response_model=CatalogSummaryOut)
def providers_catalog(_: ApiKey = Depends(require_api_key)) -> CatalogSummaryOut:
    from providers.catalog import catalog_summary

    return CatalogSummaryOut(**catalog_summary())


@router.get("/providers/catalog/search", response_model=list[CatalogExtractorOut])
def providers_catalog_search(
    q: str,
    _: ApiKey = Depends(require_api_key),
    limit: int = 50,
) -> list[CatalogExtractorOut]:
    from providers.catalog import search_extractors

    return [CatalogExtractorOut(**e) for e in search_extractors(q, limit=limit)]


@router.get("/plugins", response_model=list[PluginOut])
def list_plugins(_: ApiKey = Depends(require_api_key)) -> list[PluginOut]:
    plugins = get_plugin_loader().list()
    out: list[PluginOut] = []
    for p in plugins:
        data = p.to_dict()
        runtime = plugin_runtime_status(data["name"])
        if runtime != "stub" or data["name"].startswith("mediacore-plugin-"):
            if data["name"] in {
                "mediacore-plugin-webhook",
                "mediacore-plugin-telegram",
                "mediacore-plugin-discord",
            }:
                data["status"] = runtime
        out.append(PluginOut(**data))
    return out


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
        ffmpeg=_ffmpeg_ready(),
        events_retained=len(get_event_bus().history(1000)),
    )
