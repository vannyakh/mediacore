import pytest

from packages.config.settings import MediaCoreSettings

pytestmark = pytest.mark.unit


def test_settings_defaults():
    s = MediaCoreSettings(use_sqlite=True)
    assert s.app_name == "MediaCore"
    assert s.use_sqlite is True
