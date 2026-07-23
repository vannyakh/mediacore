"""MediaCore processing pipeline stages."""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any


class PipelineStage(str, Enum):
    URL = "url"
    ANALYZE = "analyze"
    METADATA = "metadata"
    MANIFEST = "manifest"
    FORMATS = "formats"
    DOWNLOAD = "download"
    PROCESSING = "processing"
    EXPORT = "export"
    EVENTS = "events"


PIPELINE_ORDER: list[PipelineStage] = [
    PipelineStage.URL,
    PipelineStage.ANALYZE,
    PipelineStage.METADATA,
    PipelineStage.MANIFEST,
    PipelineStage.FORMATS,
    PipelineStage.DOWNLOAD,
    PipelineStage.PROCESSING,
    PipelineStage.EXPORT,
    PipelineStage.EVENTS,
]


@dataclass
class PipelineContext:
    url: str
    stage: PipelineStage = PipelineStage.URL
    metadata: dict[str, Any] | None = None
    formats: list[dict[str, Any]] = field(default_factory=list)
    artifact_path: str | None = None
    error: str | None = None
    extras: dict[str, Any] = field(default_factory=dict)

    def advance(self, stage: PipelineStage) -> None:
        self.stage = stage

    def to_dict(self) -> dict[str, Any]:
        return {
            "url": self.url,
            "stage": self.stage.value,
            "metadata": self.metadata,
            "formats": self.formats,
            "artifact_path": self.artifact_path,
            "error": self.error,
            "extras": self.extras,
        }


class Pipeline:
    """Tracks progress through the MediaCore media workflow."""

    def __init__(self, url: str) -> None:
        self.ctx = PipelineContext(url=url)

    def set_metadata(self, metadata: dict[str, Any]) -> None:
        self.ctx.metadata = metadata
        self.ctx.formats = list(metadata.get("formats") or [])
        self.ctx.advance(PipelineStage.METADATA)

    def set_downloaded(self, path: str) -> None:
        self.ctx.artifact_path = path
        self.ctx.advance(PipelineStage.DOWNLOAD)

    def fail(self, message: str) -> None:
        self.ctx.error = message

    def snapshot(self) -> dict[str, Any]:
        return self.ctx.to_dict()
