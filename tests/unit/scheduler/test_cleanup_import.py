import pytest

from packages.scheduler import cleanup_expired_jobs

pytestmark = pytest.mark.unit


def test_cleanup_callable():
    assert callable(cleanup_expired_jobs)
