from pathlib import Path

import pytest

from packages.storage.local import LocalStorage
from packages.testkit.contracts import run_storage_contract
from packages.testkit.fake_storage import FakeStorage

pytestmark = pytest.mark.storage


def test_local_storage_contract(tmp_path: Path, monkeypatch):
    monkeypatch.setenv("STORAGE_ROOT", str(tmp_path / "local"))
    from apps.api.config import get_settings

    get_settings.cache_clear()
    storage = LocalStorage(root=tmp_path / "local")
    run_storage_contract(storage, tmp_path)
    get_settings.cache_clear()


def test_fake_storage_contract(tmp_path: Path):
    storage = FakeStorage(tmp_path / "fake")
    run_storage_contract(storage, tmp_path)


@pytest.mark.parametrize("backend", ["s3", "gdrive", "r2", "ftp", "webdav"])
def test_remote_storage_not_implemented(backend: str):
    pytest.skip(f"{backend} storage backend not implemented yet")
