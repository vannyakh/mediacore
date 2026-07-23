from pathlib import Path
from unittest.mock import patch

import pytest

from packages.core.exceptions import UnsupportedURLError
from packages.engine.engine import MediaCoreEngine
from packages.plugins.loader import PluginInfo, PluginLoader
from packages.registry.providers import ProviderRegistry

pytestmark = pytest.mark.chaos


def test_engine_unsupported_url_graceful():
    engine = MediaCoreEngine(registry=ProviderRegistry())
    with pytest.raises(UnsupportedURLError):
        engine.analyze("https://unknown.example/nope")


def test_plugin_loader_bad_manifest(tmp_path: Path):
    bad = tmp_path / "broken"
    bad.mkdir()
    (bad / "plugin.py").write_text("raise RuntimeError('boom')\n", encoding="utf-8")
    loader = PluginLoader(root=tmp_path)
    plugins = loader.discover()
    assert len(plugins) == 1
    assert plugins[0].status == "error"


def test_queue_falls_back_when_send_fails(monkeypatch):
    monkeypatch.setenv("DRAMATIQ_STUB", "false")
    monkeypatch.setenv("SYNC_DOWNLOAD", "false")
    from packages.queue import broker

    # Reset broker flag so configure isn't sticky for this assertion path
    with (
        patch("apps.worker.actors.download_job") as dj,
        patch("apps.worker.actors.run_download_sync") as sync,
    ):
        dj.send.side_effect = RuntimeError("redis down")
        broker.enqueue_download("chaos-job")
        sync.assert_called_once_with("chaos-job")


def test_fake_plugin_info_survives_list():
    info = PluginInfo(name="mediacore-plugin-x", status="error", description="fail")
    assert info.to_dict()["status"] == "error"
