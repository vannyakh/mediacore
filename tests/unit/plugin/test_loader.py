from pathlib import Path

import pytest

from packages.plugins.kinds import PluginKind
from packages.plugins.loader import PluginLoader

pytestmark = pytest.mark.unit


def test_discover_builtin_plugins():
    loader = PluginLoader()
    plugins = loader.discover()
    names = {p.name for p in plugins}
    assert "mediacore-plugin-storage-local" in names
    assert "mediacore-plugin-ffmpeg" in names
    assert "mediacore-plugin-metadata" in names
    assert "mediacore-plugin-auth-apikey" in names


def test_stub_plugin_dirs():
    loader = PluginLoader()
    stubs = [p for p in loader.discover() if p.status == "stub"]
    # OAuth / vendor clouds remain stubs until fully wired
    assert any(p.name.endswith("storage-gdrive") for p in stubs)
    assert any(p.name.endswith("storage-azure") for p in stubs)


def test_loader_get():
    loader = PluginLoader()
    loader.discover()
    info = loader.get("mediacore-plugin-storage-local")
    assert info is not None
    assert "store" in info.capabilities
    assert info.kind == PluginKind.STORAGE.value


def test_by_kind():
    loader = PluginLoader()
    loader.discover()
    storage = loader.by_kind(PluginKind.STORAGE)
    assert any(p.name == "mediacore-plugin-storage-local" for p in storage)
    ffmpeg = loader.by_kind("ffmpeg")
    assert len(ffmpeg) == 1
    assert ffmpeg[0].name == "mediacore-plugin-ffmpeg"


def test_unknown_kind_becomes_error(tmp_path: Path):
    plugin_dir = tmp_path / "demo"
    plugin_dir.mkdir()
    (plugin_dir / "plugin.py").write_text(
        'PLUGIN = {"name": "mediacore-plugin-demo", "kind": "demo", "capabilities": ["x"]}\n',
        encoding="utf-8",
    )
    loader = PluginLoader(root=tmp_path)
    plugins = loader.discover()
    assert len(plugins) == 1
    assert plugins[0].status == "error"


def test_custom_plugin_root(tmp_path: Path):
    plugin_dir = tmp_path / "demo"
    plugin_dir.mkdir()
    (plugin_dir / "plugin.py").write_text(
        'PLUGIN = {"name": "mediacore-plugin-demo", "kind": "storage", "capabilities": ["x"]}\n',
        encoding="utf-8",
    )
    loader = PluginLoader(root=tmp_path)
    plugins = loader.discover()
    assert len(plugins) == 1
    assert plugins[0].name == "mediacore-plugin-demo"
    assert plugins[0].kind == "storage"
