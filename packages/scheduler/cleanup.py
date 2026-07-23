"""Shared cleanup helpers used by apps.scheduler."""

from __future__ import annotations

from datetime import datetime, timedelta, timezone

from sqlalchemy import select

from apps.api.db.models import Job, JobStatus
from apps.api.db.session import SessionLocal
from packages.config.settings import get_settings
from packages.queue.broker import enqueue_cleanup


def cleanup_expired_jobs() -> int:
    settings = get_settings()
    cutoff = datetime.now(timezone.utc) - timedelta(hours=settings.job_ttl_hours)
    count = 0
    with SessionLocal() as db:
        jobs = db.scalars(
            select(Job).where(
                Job.status == JobStatus.completed,
                Job.completed_at.is_not(None),
                Job.completed_at < cutoff,
            )
        ).all()
        for job in jobs:
            enqueue_cleanup(job.id)
            count += 1
    return count
