from pathlib import Path

import pytest

from packages.plugins.loader import reset_plugin_loader
from packages.storage.factory import BACKEND_PLUGINS, normalize_backend, resolve_storage

pytestmark = pytest.mark.unit


def test_normalize_backend_aliases():
    assert normalize_backend(None) == "local"
    assert normalize_backend("Google-Drive") == "gdrive"
    assert normalize_backend("azure_blob") == "azure"


def test_all_documented_backends_mapped():
    expected = {
        "local",
        "s3",
        "r2",
        "gdrive",
        "azure",
        "dropbox",
        "onedrive",
        "ftp",
        "webdav",
    }
    assert expected.issubset(set(BACKEND_PLUGINS))


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
