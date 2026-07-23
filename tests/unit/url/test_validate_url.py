import pytest

from packages.core.validator import validate_url

pytestmark = pytest.mark.unit


def test_https_ok():
    assert validate_url("https://cdn.example.com/a.mp4")
