import pytest

from packages.core.models import FormatInfo, MediaMetadata
from packages.plugins.services import (
    ApiKeyAuthAdapter,
    MetadataNormalizer,
    get_analytics_sink,
    reset_analytics_sink,
)

pytestmark = pytest.mark.unit


def test_metadata_normalizer_enrich():
    meta = MediaMetadata(
        platform="generic",
        url="https://cdn.example.com/a.mp4",
        title="  hello   world  ",
        formats=[FormatInfo(id="original", quality="original", container="mp4")],
    )
    out = MetadataNormalizer().enrich(meta)
    assert out.title == "hello world"
    assert out.extra.get("normalized") is True
    assert out.extra.get("format_hint") == "mp4"


def test_api_key_adapter():
    auth = ApiKeyAuthAdapter()
    h = auth.hash("secret")
    assert auth.verify("secret", h)
    assert not auth.verify("nope", h)


def test_analytics_sink_tracks_events():
    reset_analytics_sink()
    sink = get_analytics_sink()

    class E:
        type = type("T", (), {"value": "Completed"})()
        payload = {"job_id": "1"}

    sink.on_event(E())
    metrics = sink.metrics()
    assert metrics["counts"]["Completed"] == 1
    assert metrics["total"] == 1
    reset_analytics_sink()
