"""In-process event bus for MediaCore job lifecycle."""

from __future__ import annotations

import logging
from collections import defaultdict
from collections.abc import Callable
from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from typing import Any

logger = logging.getLogger("mediacore.events")

EVENTS_CHANNEL = "mediacore:events"


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
Publisher = Callable[[dict[str, Any]], None]


class EventBus:
    def __init__(self, *, retain: int = 200) -> None:
        self._listeners: dict[EventType | None, list[Listener]] = defaultdict(list)
        self._history: list[Event] = []
        self._retain = retain
        self._publisher: Publisher | None = None

    def set_publisher(self, publisher: Publisher | None) -> None:
        self._publisher = publisher

    def on(self, event_type: EventType | None, listener: Listener) -> None:
        self._listeners[event_type].append(listener)

    def off(self, event_type: EventType | None, listener: Listener) -> None:
        listeners = self._listeners.get(event_type)
        if not listeners:
            return
        try:
            listeners.remove(listener)
        except ValueError:
            return

    def emit(self, event_type: EventType, *, remote: bool = False, **payload: Any) -> Event:
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
        try:
            from packages.plugins.runtime import get_runtime

            get_runtime().dispatch_event(event)
        except Exception:  # noqa: BLE001
            logger.exception("Plugin event dispatch failed for %s", event_type)
        if not remote and self._publisher is not None:
            try:
                self._publisher(event.to_dict())
            except Exception:  # noqa: BLE001
                logger.exception("Event publish failed for %s", event_type)
        logger.debug("event %s %s", event_type.value, payload)
        return event

    def emit_remote(self, data: dict[str, Any]) -> Event | None:
        """Ingest an event received from Redis without re-publishing."""
        try:
            event_type = EventType(data["type"])
        except (KeyError, ValueError):
            logger.warning("Ignoring malformed remote event: %s", data)
            return None
        payload = dict(data.get("payload") or {})
        at = data.get("at")
        event = Event(type=event_type, payload=payload, at=at or Event().at)
        self._history.append(event)
        if len(self._history) > self._retain:
            self._history = self._history[-self._retain :]
        for listener in list(self._listeners.get(event_type, [])) + list(
            self._listeners.get(None, [])
        ):
            try:
                listener(event)
            except Exception:  # noqa: BLE001
                logger.exception("Event listener failed for remote %s", event_type)
        try:
            from packages.plugins.runtime import get_runtime

            get_runtime().dispatch_event(event)
        except Exception:  # noqa: BLE001
            logger.exception("Plugin event dispatch failed for remote %s", event_type)
        return event

    def history(self, limit: int = 50, *, job_id: str | None = None) -> list[dict[str, Any]]:
        items = self._history
        if job_id is not None:
            items = [e for e in items if e.payload.get("job_id") == job_id]
        return [e.to_dict() for e in items[-limit:]]

    def clear(self) -> None:
        self._history.clear()


_bus: EventBus | None = None


def get_event_bus() -> EventBus:
    global _bus
    if _bus is None:
        _bus = EventBus()
    return _bus


def reset_event_bus() -> EventBus:
    """Replace the process-global bus (tests / process restart)."""
    global _bus
    _bus = EventBus()
    return _bus
