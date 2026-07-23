from pathlib import Path

import pytest

from packages.plugins.loader import PluginLoader

pytestmark = pytest.mark.unit


def test_discover_builtin_plugins():
    loader = PluginLoader()
    plugins = loader.discover()
    names = {p.name for p in plugins}
    assert "mediacore-plugin-storage-local" in names
    assert "mediacore-plugin-ffmpeg" in names


def test_stub_plugin_dirs():
    loader = PluginLoader()
    stubs = [p for p in loader.discover() if p.status == "stub"]
    assert any(p.name.endswith("storage-s3") for p in stubs)


def test_loader_get():
    loader = PluginLoader()
    loader.discover()
    info = loader.get("mediacore-plugin-storage-local")
    assert info is not None
    assert "store" in info.capabilities


def test_custom_plugin_root(tmp_path: Path):
    plugin_dir = tmp_path / "demo"
    plugin_dir.mkdir()
    (plugin_dir / "plugin.py").write_text(
        'PLUGIN = {"name": "mediacore-plugin-demo", "kind": "demo", "capabilities": ["x"]}\n',
        encoding="utf-8",
    )
    loader = PluginLoader(root=tmp_path)
    plugins = loader.discover()
    assert len(plugins) == 1
    assert plugins[0].name == "mediacore-plugin-demo"
