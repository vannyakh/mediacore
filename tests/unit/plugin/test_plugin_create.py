from pathlib import Path
from unittest.mock import MagicMock

import pytest

from packages.core.exceptions import PluginError
from packages.plugins.loader import PluginLoader, reset_plugin_loader
from packages.plugins.runtime import PluginRuntime, reset_runtime
from packages.plugins.services import reset_analytics_sink

pytestmark = pytest.mark.unit


@pytest.fixture(autouse=True)
def _reset():
    reset_plugin_loader()
    reset_runtime()
    reset_analytics_sink()
    yield
    reset_plugin_loader()
    reset_runtime()
    reset_analytics_sink()


def test_ffmpeg_create_service():
    runtime = PluginRuntime(loader=PluginLoader())
    svc = runtime.ffmpeg()
    assert hasattr(svc, "extract_audio")
    assert hasattr(svc, "convert")


def test_metadata_plugin_create():
    runtime = PluginRuntime(loader=PluginLoader())
    norm = runtime.metadata_normalizer()
    assert hasattr(norm, "enrich")


def test_analytics_plugin_available():
    loader = PluginLoader()
    info = loader.get("mediacore-plugin-analytics")
    assert info is not None
    assert info.status == "available"
    assert "on_event" in (info.module or {})


def test_auth_apikey_create():
    runtime = PluginRuntime(loader=PluginLoader())
    auth = runtime.create("mediacore-plugin-auth-apikey")
    assert auth.verify("k", auth.hash("k"))


def test_provider_bridge_resolve():
    runtime = PluginRuntime(loader=PluginLoader())
    bridge = runtime.create("mediacore-plugin-provider")
    # Direct media → generic
    p = bridge.resolve("https://cdn.example.com/x.mp4")
    assert p.name == "generic"


def test_azure_create_requires_config(tmp_path: Path):
    settings = MagicMock()
    settings.azure_storage_connection_string = None
    settings.azure_storage_container = None
    settings.storage_root = str(tmp_path)
    loader = PluginLoader()
    info = loader.get("mediacore-plugin-storage-azure")
    assert info is not None
    assert info.status == "available"
    create = (info.module or {})["create"]
    with pytest.raises(PluginError, match="Azure"):
        create(settings, root=tmp_path)
