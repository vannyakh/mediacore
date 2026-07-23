"""Load tests run via Locust CLI, not pytest import (gevent patches conflict)."""

from pathlib import Path

import pytest

pytestmark = pytest.mark.load


def test_locustfile_exists():
    path = Path(__file__).with_name("locustfile.py")
    assert path.is_file()
    text = path.read_text(encoding="utf-8")
    assert "MediaCoreUser" in text
    assert "/health" in text
