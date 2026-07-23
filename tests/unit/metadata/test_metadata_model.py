import pytest

from packages.core.models import FormatInfo, MediaMetadata

pytestmark = pytest.mark.unit


def test_metadata_formats():
    meta = MediaMetadata(
        platform="generic",
        url="https://x/a.mp4",
        title="a",
        formats=[FormatInfo(id="original", quality="original", container="mp4")],
    )
    assert len(meta.formats) == 1
