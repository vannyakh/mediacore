import pytest

from packages.core.models import MediaMetadata

pytestmark = pytest.mark.unit


def test_manifest_roundtrip():
    meta = MediaMetadata(
        platform="generic",
        url="https://cdn.example.com/a.mp4",
        title="a",
        manifest={"type": "direct"},
    )
    assert meta.to_dict()["manifest"]["type"] == "direct"
