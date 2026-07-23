import pytest

from packages.storage.local import LocalStorage

pytestmark = pytest.mark.integration


def test_local_storage_roundtrip(storage_root):
    storage = LocalStorage(root=storage_root)
    path = storage.path_for("job-int", "media.bin")
    path.write_bytes(b"payload")
    assert path.read_bytes() == b"payload"
    assert storage.public_url("job-int", "media.bin").startswith("/files/")
    storage.delete_job("job-int")
    assert not path.exists()
