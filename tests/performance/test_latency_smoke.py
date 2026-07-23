import pytest

from packages.core.parser import hostname, is_direct_media_url
from packages.core.validator import validate_url
from packages.testkit.performance import assert_latency_under

pytestmark = pytest.mark.performance


def test_validator_latency():
    assert_latency_under(
        lambda: validate_url("https://cdn.example.com/a.mp4"),
        max_ms=5.0,
        iterations=100,
    )


def test_parser_latency():
    url = "https://cdn.example.com/path/to/video.mp4?x=1"

    def work():
        hostname(url)
        is_direct_media_url(url)

    assert_latency_under(work, max_ms=5.0, iterations=100)
