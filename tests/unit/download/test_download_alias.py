import pytest

from packages.core import downloader

pytestmark = pytest.mark.unit


def test_downloader_exports():
    assert hasattr(downloader, "download_file")
