"""End-to-end: URL → analyze → download → file on disk (FakeProvider)."""

from pathlib import Path

import pytest

from packages.engine.engine import MediaCoreEngine
from packages.registry.providers import ProviderRegistry
from packages.testkit.fake_provider import FakeProvider
from packages.testkit.fake_storage import FakeStorage

pytestmark = pytest.mark.e2e


def test_analyze_download_export(tmp_path: Path):
    registry = ProviderRegistry()
    registry.register(FakeProvider(payload=b"e2e-bytes"))
    engine = MediaCoreEngine(registry=registry)
    storage = FakeStorage(tmp_path / "out")

    url = "https://fake.mediacore.test/clip.mp4"
    meta = engine.analyze(url)
    assert meta.title
    formats = engine.list_formats(url)
    format_id = formats[0].id

    dest = storage.path_for("e2e-job", f"export.{formats[0].container}")
    result = engine.download(url, format_id, dest)

    assert result.path.exists()
    assert result.path.read_bytes() == b"e2e-bytes"
    assert storage.public_url("e2e-job", dest.name).startswith("/files/e2e-job/")
