from pathlib import Path
from unittest.mock import patch

import pytest

from providers.generic.provider import GenericHTTPProvider

pytestmark = pytest.mark.provider


def test_generic_metadata():
    provider = GenericHTTPProvider()
    with patch("providers.generic.provider.head_content_type", return_value="video/mp4"):
        meta = provider.get_metadata("https://cdn.example.com/demo.mp4")
    assert meta.platform == "generic"
    assert meta.title == "demo.mp4"
    assert meta.formats[0].id == "original"
    assert meta.manifest is not None


def test_generic_download(tmp_path: Path):
    provider = GenericHTTPProvider()
    dest = tmp_path / "out.mp4"
    with (
        patch("providers.generic.provider.head_content_type", return_value="video/mp4"),
        patch(
            "providers.generic.provider.download_file",
            return_value=(128, "video/mp4"),
        ) as mock_dl,
    ):
        result = provider.download("https://cdn.example.com/demo.mp4", "original", dest)
    mock_dl.assert_called_once()
    assert result.format_id == "original"
    assert result.filesize == 128
