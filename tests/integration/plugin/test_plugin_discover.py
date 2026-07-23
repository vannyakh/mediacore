import pytest

from packages.plugins.loader import PluginLoader

pytestmark = pytest.mark.integration


def test_discover_list_get():
    loader = PluginLoader()
    discovered = loader.discover()
    listed = loader.list()
    assert len(listed) == len(discovered)
    first = listed[0]
    assert loader.get(first.name) is not None
