import pytest

from packages.events.bus import EventBus, EventType

pytestmark = pytest.mark.unit


def test_event_bus():
    bus = EventBus()
    seen = []
    bus.on(EventType.JOB_CREATED, lambda e: seen.append(e.type))
    bus.emit(EventType.JOB_CREATED, job_id="1")
    assert seen == [EventType.JOB_CREATED]
    assert len(bus.history()) == 1


def test_history_job_filter():
    bus = EventBus()
    bus.emit(EventType.JOB_CREATED, job_id="a")
    bus.emit(EventType.PROGRESS, job_id="b", percent=10)
    bus.emit(EventType.PROGRESS, job_id="a", percent=50)
    hist = bus.history(10, job_id="a")
    assert len(hist) == 2
    assert all(h["payload"]["job_id"] == "a" for h in hist)


def test_off_removes_listener():
    bus = EventBus()
    seen: list[str] = []

    def listener(e):
        seen.append(e.type.value)

    bus.on(None, listener)
    bus.emit(EventType.FAILED, job_id="1")
    bus.off(None, listener)
    bus.emit(EventType.FAILED, job_id="2")
    assert seen == ["Failed"]


def test_publisher_called_once_local():
    bus = EventBus()
    published: list[dict] = []
    bus.set_publisher(published.append)
    bus.emit(EventType.CANCELLED, job_id="x")
    assert len(published) == 1
    assert published[0]["type"] == "Cancelled"


def test_emit_remote_does_not_publish():
    bus = EventBus()
    published: list[dict] = []
    bus.set_publisher(published.append)
    bus.emit_remote({"type": "Progress", "payload": {"job_id": "1", "percent": 1}, "at": "t"})
    assert published == []
    assert bus.history(1)[0]["type"] == "Progress"
