from pathlib import Path

import pytest

from packages.registry.providers import ProviderRegistry
from packages.testkit.fake_provider import FakeProvider
from packages.testkit.fake_storage import FakeStorage

pytestmark = pytest.mark.integration


def test_registry_download_to_storage(tmp_path: Path):
    registry = ProviderRegistry()
    provider = FakeProvider()
    registry.register(provider)
    storage = FakeStorage(tmp_path / "files")

    url = "https://fake.mediacore.test/a.mp4"
    resolved = registry.resolve(url)
    dest = storage.path_for("job-1", "out.mp4")
    result = resolved.download(url, "original", dest)

    assert result.path.exists()
    assert storage.path_for("job-1", "out.mp4").read_bytes() == b"fake-media-bytes"
