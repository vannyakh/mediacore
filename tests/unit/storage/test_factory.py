from pathlib import Path

import pytest

from packages.core.exceptions import PluginError
from packages.plugins.loader import reset_plugin_loader
from packages.storage.factory import BACKEND_PLUGINS, normalize_backend, resolve_storage

pytestmark = pytest.mark.unit


def test_normalize_backend_local():
    assert normalize_backend(None) == "local"
    assert normalize_backend("LOCAL") == "local"


def test_slim_backends_local_only():
    assert set(BACKEND_PLUGINS) == {"local"}


def test_local_does_not_require_cloud(tmp_path: Path, monkeypatch):
    monkeypatch.setenv("STORAGE_BACKEND", "local")
    monkeypatch.setenv("STORAGE_ROOT", str(tmp_path))
    from packages.config.settings import get_settings

    get_settings.cache_clear()
    reset_plugin_loader()
    storage = resolve_storage(root=tmp_path)
    p = storage.path_for("j1", "f.bin")
    p.write_bytes(b"x")
    assert storage.publish("j1", p) == "/files/j1/f.bin"
    get_settings.cache_clear()


def test_unknown_backend_fails(tmp_path: Path, monkeypatch):
    monkeypatch.setenv("STORAGE_BACKEND", "s3")
    monkeypatch.setenv("STORAGE_ROOT", str(tmp_path))
    from packages.config.settings import get_settings

    get_settings.cache_clear()
    reset_plugin_loader()
    with pytest.raises(PluginError, match="local only"):
        resolve_storage()
    get_settings.cache_clear()
