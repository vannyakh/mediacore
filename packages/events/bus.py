"""In-process event bus for MediaCore job lifecycle."""

from __future__ import annotations

import logging
from collections import defaultdict
from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from typing import Any, Callable

logger = logging.getLogger("mediacore.events")


class EventType(str, Enum):
    JOB_CREATED = "JobCreated"
    ANALYZE_STARTED = "AnalyzeStarted"
    METADATA_READY = "MetadataReady"
    DOWNLOAD_STARTED = "DownloadStarted"
    PROGRESS = "Progress"
    PROCESSING_STARTED = "ProcessingStarted"
    COMPLETED = "Completed"
    FAILED = "Failed"
    CANCELLED = "Cancelled"


@dataclass
class Event:
    type: EventType
    payload: dict[str, Any] = field(default_factory=dict)
    at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())

    def to_dict(self) -> dict[str, Any]:
        return {"type": self.type.value, "payload": self.payload, "at": self.at}


Listener = Callable[[Event], None]


class EventBus:
    def __init__(self, *, retain: int = 200) -> None:
        self._listeners: dict[EventType | None, list[Listener]] = defaultdict(list)
        self._history: list[Event] = []
        self._retain = retain

    def on(self, event_type: EventType | None, listener: Listener) -> None:
        self._listeners[event_type].append(listener)

    def emit(self, event_type: EventType, **payload: Any) -> Event:
        event = Event(type=event_type, payload=payload)
        self._history.append(event)
        if len(self._history) > self._retain:
            self._history = self._history[-self._retain :]
        for listener in list(self._listeners.get(event_type, [])) + list(
            self._listeners.get(None, [])
        ):
            try:
                listener(event)
            except Exception:  # noqa: BLE001
                logger.exception("Event listener failed for %s", event_type)
        logger.debug("event %s %s", event_type.value, payload)
        return event

    def history(self, limit: int = 50) -> list[dict[str, Any]]:
        return [e.to_dict() for e in self._history[-limit:]]


_bus: EventBus | None = None


def get_event_bus() -> EventBus:
    global _bus
    if _bus is None:
        _bus = EventBus()
    return _bus
