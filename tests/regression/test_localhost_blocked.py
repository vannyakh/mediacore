"""Regression: private/local hosts must be rejected by default."""

import pytest

from packages.core.exceptions import InvalidURLError
from packages.core.validator import validate_url

pytestmark = pytest.mark.regression


@pytest.mark.parametrize(
    "url",
    [
        "http://localhost/video.mp4",
        "http://127.0.0.1/video.mp4",
        "http://0.0.0.0/video.mp4",
        "http://[::1]/video.mp4",
        "http://169.254.169.254/latest/meta-data",
    ],
)
def test_private_hosts_rejected(url: str):
    with pytest.raises(InvalidURLError):
        validate_url(url)
