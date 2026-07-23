import pytest

from packages.events.bus import Event, EventBus, EventType
from packages.events.plugins import forward_webhook, register_event_plugins

pytestmark = pytest.mark.unit


def test_forward_webhook_posts(monkeypatch):
    calls = []

    class FakeClient:
        def __init__(self, *a, **k):
            pass

        def __enter__(self):
            return self

        def __exit__(self, *a):
            return False

        def post(self, url, json=None):
            calls.append((url, json))
            return type("R", (), {"status_code": 200})()

    monkeypatch.setattr("packages.events.plugins.httpx.Client", FakeClient)
    event = Event(type=EventType.JOB_CREATED, payload={"job_id": "1"})
    forward_webhook(event, url="https://hooks.example.com/mc")
    assert calls == [("https://hooks.example.com/mc", event.to_dict())]


def test_register_event_plugins_when_url_set(monkeypatch):
    monkeypatch.setenv("MEDIACORE_WEBHOOK_URL", "https://hooks.example.com/mc")
    from apps.api.config import get_settings

    get_settings.cache_clear()
    bus = EventBus()
    calls = []

    class FakeClient:
        def __init__(self, *a, **k):
            pass

        def __enter__(self):
            return self

        def __exit__(self, *a):
            return False

        def post(self, url, json=None):
            calls.append(url)
            return type("R", (), {"status_code": 200})()

    monkeypatch.setattr("packages.events.plugins.httpx.Client", FakeClient)
    enabled = register_event_plugins(bus)
    assert "mediacore-plugin-webhook" in enabled
    bus.emit(EventType.COMPLETED, job_id="z")
    assert "https://hooks.example.com/mc" in calls
    get_settings.cache_clear()
