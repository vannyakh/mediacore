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
