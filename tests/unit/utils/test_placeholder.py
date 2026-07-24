import pytest

from packages.core.parser import quality_from_height

pytestmark = pytest.mark.unit


def test_quality_from_height():
    assert quality_from_height(720) == "720p"
    assert quality_from_height(None) == "original"
