from __future__ import annotations

import json

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from apps.api.config import get_settings
from apps.api.db.models import ApiKey, Job, JobStatus
from apps.api.db.session import get_db
from apps.api.middleware.auth import require_api_key
from apps.api.schemas import DownloadRequest, DownloadResponse, JobResponse
from extractor.core.engine import ExtractorEngine
from extractor.core.exceptions import ExtractorError
from jobqueue.broker import enqueue_download

router = APIRouter(prefix="/api/v1", tags=["jobs"])


@router.post("/download", response_model=DownloadResponse, status_code=status.HTTP_202_ACCEPTED)
def create_download(
    body: DownloadRequest,
    api_key: ApiKey = Depends(require_api_key),
    db: Session = Depends(get_db),
) -> DownloadResponse:
    settings = get_settings()
    engine = ExtractorEngine()
    try:
        meta = engine.analyze(body.url, allow_private=settings.allow_private_urls)
    except ExtractorError as exc:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={"error": exc.message, "code": exc.code},
        ) from exc

    job = Job(
        user_id=api_key.user_id,
        api_key_id=api_key.id,
        type="download",
        status=JobStatus.queued,
        url=body.url,
        platform=meta.platform,
        format_id=body.format,
        meta_json=json.dumps(meta.to_dict()),
    )
    db.add(job)
    db.commit()
    db.refresh(job)

    enqueue_download(job.id)
    return DownloadResponse(job_id=job.id, status=job.status.value)


@router.get("/jobs/{job_id}", response_model=JobResponse)
def get_job(
    job_id: str,
    _: ApiKey = Depends(require_api_key),
    db: Session = Depends(get_db),
) -> JobResponse:
    job = db.scalar(select(Job).where(Job.id == job_id))
    if job is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Job not found")
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
