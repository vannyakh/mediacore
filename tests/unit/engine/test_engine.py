from pathlib import Path

import pytest

from packages.engine.engine import MediaCoreEngine
from packages.registry.providers import ProviderRegistry
from packages.testkit.fake_provider import FakeProvider

pytestmark = pytest.mark.unit


@pytest.fixture()
def engine() -> MediaCoreEngine:
    registry = ProviderRegistry()
    registry.register(FakeProvider())
    return MediaCoreEngine(registry=registry)


def test_analyze(engine: MediaCoreEngine):
    meta = engine.analyze("https://fake.mediacore.test/clip.mp4")
    assert meta.platform == "fake"
    assert meta.formats[0].id == "original"
    assert meta.manifest is not None


def test_list_formats(engine: MediaCoreEngine):
    formats = engine.list_formats("https://fake.mediacore.test/clip.mp4")
    assert formats[0].id == "original"


def test_download(engine: MediaCoreEngine, tmp_path: Path):
    dest = tmp_path / "out.mp4"
    result = engine.download("https://fake.mediacore.test/clip.mp4", "original", dest)
    assert result.path.exists()
    assert result.filesize == len(b"fake-media-bytes")


def test_providers(engine: MediaCoreEngine):
    names = {p["name"] for p in engine.providers()}
    assert "fake" in names
