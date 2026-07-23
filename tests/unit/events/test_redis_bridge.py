import json

import pytest

from packages.events.bus import EventBus, EventType
from packages.events.redis_bridge import RedisEventBridge

pytestmark = pytest.mark.unit


class FakeRedis:
    def __init__(self):
        self.published: list[tuple[str, str]] = []

    def publish(self, channel: str, message: str) -> int:
        self.published.append((channel, message))
        return 1

    def close(self) -> None:
        return None


def test_attach_publisher_publishes_json(monkeypatch):
    bus = EventBus()
    bridge = RedisEventBridge(bus, "redis://localhost:6379/0")
    fake = FakeRedis()
    monkeypatch.setattr(bridge, "_redis", lambda: fake)
    bridge.attach_publisher()
    bus.emit(EventType.JOB_CREATED, job_id="j1")
    assert len(fake.published) == 1
    channel, raw = fake.published[0]
    assert channel == "mediacore:events"
    data = json.loads(raw)
    assert data["type"] == "JobCreated"
    assert data["payload"]["job_id"] == "j1"


def test_emit_remote_roundtrip_no_echo(monkeypatch):
    bus = EventBus()
    bridge = RedisEventBridge(bus, "redis://localhost:6379/0")
    fake = FakeRedis()
    monkeypatch.setattr(bridge, "_redis", lambda: fake)
    bridge.attach_publisher()
    seen = []
    bus.on(None, lambda e: seen.append(e.type))
    bus.emit_remote(
        {
            "type": "MetadataReady",
            "payload": {"job_id": "j2", "title": "x"},
            "at": "2026-01-01T00:00:00+00:00",
        }
    )
    assert seen == [EventType.METADATA_READY]
    assert fake.published == []
