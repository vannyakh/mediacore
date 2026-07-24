import pytest

from packages.core.exceptions import FormatNotFoundError
from packages.core.format_select import select_format_id
from packages.core.models import FormatInfo

pytestmark = pytest.mark.unit


def test_select_explicit():
    formats = [
        FormatInfo(id="a", quality="1", container="mp4"),
        FormatInfo(id="b", quality="2", container="webm"),
    ]
    assert select_format_id(formats, "b") == "b"


def test_select_default_prefers_mp4():
    formats = [
        FormatInfo(id="x.webm", quality="hd", container="webm"),
        FormatInfo(id="x.mp4", quality="hd", container="mp4"),
    ]
    assert select_format_id(formats, "original") == "x.mp4"


def test_select_missing_raises():
    formats = [FormatInfo(id="a", quality="1", container="mp4")]
    with pytest.raises(FormatNotFoundError):
        select_format_id(formats, "nope")
