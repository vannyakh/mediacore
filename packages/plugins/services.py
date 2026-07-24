"""Shared lightweight services used by first-party plugins."""

from __future__ import annotations

import logging
import re
from collections import Counter
from dataclasses import dataclass, field
from typing import Any

from packages.auth.api_keys import hash_api_key, verify_api_key
from packages.core.models import MediaMetadata

logger = logging.getLogger("mediacore.plugins.services")


@dataclass
class AnalyticsSink:
    """In-process analytics sink for job lifecycle events."""

    counts: Counter[str] = field(default_factory=Counter)
    recent: list[dict[str, Any]] = field(default_factory=list)
    retain: int = 200

    def track(self, event_type: str, payload: dict[str, Any] | None = None) -> None:
        self.counts[event_type] += 1
        self.recent.append({"type": event_type, "payload": payload or {}})
        if len(self.recent) > self.retain:
            self.recent = self.recent[-self.retain :]

    def on_event(self, event: Any) -> None:
        etype = getattr(getattr(event, "type", None), "value", None) or str(
            getattr(event, "type", "unknown")
        )
        payload = dict(getattr(event, "payload", None) or {})
        self.track(etype, payload)

    def metrics(self) -> dict[str, Any]:
        return {
            "counts": dict(self.counts),
            "total": int(sum(self.counts.values())),
            "recent": list(self.recent[-20:]),
        }


_analytics: AnalyticsSink | None = None


def get_analytics_sink() -> AnalyticsSink:
    global _analytics
    if _analytics is None:
        _analytics = AnalyticsSink()
    return _analytics


def reset_analytics_sink() -> None:
    global _analytics
    _analytics = None


@dataclass
class MetadataNormalizer:
    """Normalize / lightly enrich MediaMetadata fields."""

    def normalize(self, meta: MediaMetadata) -> MediaMetadata:
        title = (meta.title or "").strip()
        title = re.sub(r"\s+", " ", title)
        if title:
            meta.title = title
        if meta.author:
            meta.author = meta.author.strip()
        if meta.description:
            meta.description = meta.description.strip()
        if not meta.extra.get("normalized"):
            meta.extra = {**meta.extra, "normalized": True}
        return meta

    def enrich(self, meta: MediaMetadata) -> MediaMetadata:
        meta = self.normalize(meta)
        containers = sorted({f.container for f in meta.formats if f.container})
        if containers and "format_hint" not in meta.extra:
            meta.extra = {**meta.extra, "format_hint": containers[0]}
        if meta.duration is not None and meta.duration < 0:
            meta.duration = None
        return meta


@dataclass
class ApiKeyAuthAdapter:
    """Thin plugin adapter over packages.auth API-key helpers."""

    def hash(self, raw_key: str) -> str:
        return hash_api_key(raw_key)

    def verify(self, raw_key: str, key_hash: str) -> bool:
        return verify_api_key(raw_key, key_hash)
