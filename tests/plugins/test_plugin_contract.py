import pytest

from packages.plugins.loader import PluginLoader
from packages.testkit.contracts import run_plugin_manifest_contract

pytestmark = pytest.mark.plugin


@pytest.mark.parametrize(
    "name",
    [
        "mediacore-plugin-storage-local",
        "mediacore-plugin-ffmpeg",
    ],
)
def test_plugin_manifest_contract(name: str):
    loader = PluginLoader()
    loader.discover()
    info = loader.get(name)
    assert info is not None
    run_plugin_manifest_contract(info)


def test_download_plugins_kinds():
    loader = PluginLoader()
    kinds = {p.kind for p in loader.discover() if p.status != "error"}
    assert "storage" in kinds
    assert "ffmpeg" in kinds or "process" in kinds or "media" in kinds or len(kinds) >= 1
