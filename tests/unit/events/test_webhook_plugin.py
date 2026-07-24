import pytest

from packages.events.bus import Event, EventBus, EventType
from packages.events.plugins import forward_webhook, register_event_plugins
from packages.plugins.loader import reset_plugin_loader
from packages.plugins.runtime import reset_runtime

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


def test_emit_dispatches_webhook_on_event(monkeypatch):
    """Single delivery path: EventBus.emit → PluginRuntime.dispatch_event → on_event."""
    monkeypatch.setenv("MEDIACORE_WEBHOOK_URL", "https://hooks.example.com/mc")
    from apps.api.config import get_settings

    get_settings.cache_clear()
    reset_plugin_loader()
    reset_runtime()

    calls: list[str] = []

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
    bus = EventBus()
    enabled = register_event_plugins(bus)
    assert "mediacore-plugin-webhook" in enabled
    bus.emit(EventType.COMPLETED, job_id="z")
    assert calls.count("https://hooks.example.com/mc") == 1
    get_settings.cache_clear()
    reset_plugin_loader()
    reset_runtime()
