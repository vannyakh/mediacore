import pytest

from apps.api.db.models import JobStatus

pytestmark = pytest.mark.unit


def test_job_status_values():
    assert JobStatus.queued.value == "queued"
    assert JobStatus.completed.value == "completed"
