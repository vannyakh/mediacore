from pathlib import Path
from unittest.mock import patch

import pytest

from packages.core.exceptions import PluginError
from packages.plugins.loader import PluginLoader
from packages.plugins.runtime import PluginRuntime, get_storage

pytestmark = pytest.mark.unit


def test_get_storage_requires_local_plugin(tmp_path: Path):
    runtime = PluginRuntime(loader=PluginLoader())
    storage = runtime.get_storage(root=str(tmp_path / "files"))
    path = storage.path_for("j1", "a.bin")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(b"ok")
    assert path.exists()


def test_get_storage_missing_plugin(tmp_path: Path):
    loader = PluginLoader(root=tmp_path)
    loader.discover()
    runtime = PluginRuntime(loader=loader)
    with pytest.raises(PluginError, match="not found"):
        runtime.get_storage()


def test_ensure_ffmpeg_gate():
    runtime = PluginRuntime(loader=PluginLoader())
    with patch("packages.plugins.runtime.ffmpeg_available", return_value=False):
        with pytest.raises(PluginError, match="ffmpeg binary"):
            runtime.ensure_ffmpeg()


def test_resolve_by_kind_storage():
    runtime = PluginRuntime(loader=PluginLoader())
    info = runtime.resolve_by_kind("storage", prefer="mediacore-plugin-storage-local")
    assert info.name == "mediacore-plugin-storage-local"


def test_dispatch_event_noop_for_stubs():
    runtime = PluginRuntime(loader=PluginLoader())

    class _E:
        type = "Completed"
        payload = {}

    runtime.dispatch_event(_E())  # stubs without on_event: no error


def test_module_get_storage():
    storage = get_storage()
    assert storage is not None
