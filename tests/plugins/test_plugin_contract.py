import pytest

from packages.plugins.kinds import PluginKind
from packages.plugins.loader import PluginLoader
from packages.testkit.contracts import run_plugin_manifest_contract

pytestmark = pytest.mark.plugin


@pytest.mark.parametrize(
    "name",
    [
        "mediacore-plugin-storage-local",
        "mediacore-plugin-ffmpeg",
        "mediacore-plugin-webhook",
        "mediacore-plugin-metadata",
        "mediacore-plugin-auth-apikey",
        "mediacore-plugin-analytics",
        "mediacore-plugin-provider",
        "mediacore-plugin-translate",
        "mediacore-plugin-telegram",
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


def test_all_kinds_represented():
    loader = PluginLoader()
    kinds = {p.kind for p in loader.discover() if p.status != "error"}
    for kind in PluginKind:
        assert kind.value in kinds, f"missing plugin kind: {kind.value}"
