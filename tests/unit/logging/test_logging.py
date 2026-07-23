import pytest

from packages.logging.setup import get_logger, setup_logging

pytestmark = pytest.mark.unit


def test_logger_name():
    setup_logging("INFO")
    assert get_logger("mediacore.test").name == "mediacore.test"
