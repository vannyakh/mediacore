import pytest

pytestmark = pytest.mark.unit


def test_utils_package_importable():
    import extractor.utils.urls as urls

    assert urls.quality_from_height(720) == "720p"
