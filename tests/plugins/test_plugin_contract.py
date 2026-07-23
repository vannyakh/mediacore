import pytest

from packages.plugins.loader import PluginLoader
from packages.testkit.contracts import run_plugin_manifest_contract

pytestmark = pytest.mark.plugin


@pytest.mark.parametrize(
    "name",
    [
        "mediacore-plugin-storage-local",
        "mediacore-plugin-ffmpeg",
        "mediacore-plugin-webhook",
    ],
)
def test_plugin_manifest_contract(name: str):
    loader = PluginLoader()
    loader.discover()
    info = loader.get(name)
    assert info is not None
    run_plugin_manifest_contract(info)


def test_stub_plugins_marked():
    loader = PluginLoader()
    stubs = [p for p in loader.discover() if p.status == "stub"]
    assert stubs
    for info in stubs:
        run_plugin_manifest_contract(info)
