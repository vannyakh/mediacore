"""Pydantic request/response schemas for MediaCore API."""

from __future__ import annotations

from datetime import datetime
from typing import Any

from pydantic import BaseModel, Field


class AnalyzeRequest(BaseModel):
    url: str = Field(..., min_length=1)


class FormatOut(BaseModel):
    id: str
    quality: str
    container: str
    mime_type: str | None = None
    filesize: int | None = None
    width: int | None = None
    height: int | None = None


class AnalyzeResponse(BaseModel):
    platform: str
    title: str
    duration: float | None = None
    thumbnail: str | None = None
    description: str | None = None
    author: str | None = None
    formats: list[FormatOut]
    url: str | None = None
    manifest: dict[str, Any] | None = None


class DownloadRequest(BaseModel):
    url: str = Field(..., min_length=1)
    format: str = Field(default="original", min_length=1)


class MediaOpRequest(BaseModel):
    url: str | None = None
    path: str | None = None
    format: str = "original"
    options: dict[str, Any] = Field(default_factory=dict)


class JobCreateResponse(BaseModel):
    job_id: str
    status: str
    type: str


class JobResponse(BaseModel):
    id: str
    status: str
    type: str
    url: str
    platform: str | None = None
    format_id: str | None = None
    error: str | None = None
    result_url: str | None = None
    created_at: datetime | None = None
    completed_at: datetime | None = None


class ProviderOut(BaseModel):
    name: str
    status: str


class PluginOut(BaseModel):
    name: str
    version: str
    kind: str
    description: str
    status: str
    capabilities: list[str] = []
    path: str | None = None


class SystemOut(BaseModel):
    name: str
    version: str
    environment: str
    providers: int
    plugins: int
    ffmpeg: bool
    events_retained: int


class HealthResponse(BaseModel):
    status: str
    service: str
    version: str
