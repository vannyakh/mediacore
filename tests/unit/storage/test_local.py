import pytest

from packages.storage.local import LocalStorage

pytestmark = pytest.mark.unit


def test_local_storage_paths(storage_root):
    storage = LocalStorage(root=storage_root)
    d = storage.job_dir("abc")
    assert d.exists()
    assert storage.path_for("abc", "f.mp4").name == "f.mp4"
    assert storage.public_url("abc", "f.mp4") == "/files/abc/f.mp4"


def test_local_storage_delete(storage_root):
    storage = LocalStorage(root=storage_root)
    path = storage.path_for("job-del", "x.bin")
    path.write_bytes(b"x")
    storage.delete_job("job-del")
    assert not (storage_root / "job-del").exists()
