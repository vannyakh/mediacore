from pathlib import Path

import pytest

from packages.plugins.loader import PluginLoader, reset_plugin_loader
from packages.plugins.runtime import reset_runtime
from packages.storage.local import LocalStorage
from packages.testkit.contracts import run_storage_contract
from packages.testkit.fake_storage import FakeStorage

pytestmark = pytest.mark.storage


def test_local_storage_contract(tmp_path: Path, monkeypatch):
    monkeypatch.setenv("STORAGE_ROOT", str(tmp_path / "local"))
    from packages.config.settings import get_settings

    get_settings.cache_clear()
    storage = LocalStorage(root=tmp_path / "local")
    run_storage_contract(storage, tmp_path)
    get_settings.cache_clear()


def test_fake_storage_contract(tmp_path: Path):
    storage = FakeStorage(tmp_path / "fake")
    run_storage_contract(storage, tmp_path)
    url = storage.publish("job-1", storage.path_for("job-1", "a.bin"))
    assert url.endswith("/a.bin")


def test_storage_local_plugin_discovered():
    reset_plugin_loader()
    loader = PluginLoader()
    info = {p.name: p for p in loader.discover()}["mediacore-plugin-storage-local"]
    assert info.kind == "storage"
    assert "store" in info.capabilities or info.status == "stub"
    assert info.module is not None
    assert callable(info.module.get("create"))


def test_default_resolve_is_local(tmp_path: Path, monkeypatch):
    monkeypatch.setenv("STORAGE_BACKEND", "local")
    monkeypatch.setenv("STORAGE_ROOT", str(tmp_path / "files"))
    from packages.config.settings import get_settings
    from packages.storage.factory import resolve_storage

    get_settings.cache_clear()
    reset_plugin_loader()
    reset_runtime()
    storage = resolve_storage()
    assert storage.name == "local"
    assert storage.requires_cloud is False
    get_settings.cache_clear()
