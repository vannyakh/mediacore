from unittest.mock import patch

import pytest

from packages.queue import broker

pytestmark = pytest.mark.unit


def test_enqueue_download_sync(monkeypatch):
    monkeypatch.setenv("DRAMATIQ_STUB", "true")
    monkeypatch.setenv("SYNC_DOWNLOAD", "true")
    with patch("apps.worker.actors.run_download_sync") as sync:
        broker.enqueue_download("job-1")
        sync.assert_called_once_with("job-1")


def test_enqueue_process_sync(monkeypatch):
    monkeypatch.setenv("DRAMATIQ_STUB", "true")
    with patch("apps.worker.actors.run_process_sync") as sync:
        broker.enqueue_process("job-2", "audio")
        sync.assert_called_once_with("job-2", "audio")


def test_fake_queue_records():
    from packages.testkit.fake_queue import FakeQueue

    q = FakeQueue()
    q.enqueue_download("a")
    q.enqueue_process("b", "convert")
    assert q.downloads == ["a"]
    assert q.processes == [("b", "convert")]
