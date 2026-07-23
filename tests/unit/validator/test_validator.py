import pytest

from packages.core.exceptions import InvalidURLError, ValidationError
from packages.core.validator import validate_format_id, validate_url

pytestmark = pytest.mark.unit


def test_validate_https_ok():
    assert validate_url("https://cdn.example.com/a.mp4").startswith("https://")


def test_reject_localhost():
    with pytest.raises(InvalidURLError):
        validate_url("http://localhost/video.mp4")


def test_reject_non_http():
    with pytest.raises(InvalidURLError):
        validate_url("ftp://example.com/a.mp4")


def test_allow_file_scheme():
    assert validate_url("file:///tmp/a.mp4").startswith("file://")


def test_allow_private_when_flagged():
    assert validate_url("http://127.0.0.1/a.mp4", allow_private=True)


def test_reject_link_local():
    with pytest.raises(InvalidURLError):
        validate_url("http://169.254.1.1/a.mp4")


def test_validate_format_id():
    assert validate_format_id(" original ") == "original"
    with pytest.raises(ValidationError):
        validate_format_id("")
