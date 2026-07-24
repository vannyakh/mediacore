import pytest

from packages.core.models import MediaMetadata
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


def test_metadata_normalizer_identity_without_plugin():
    runtime = PluginRuntime(loader=PluginLoader())
    norm = runtime.metadata_normalizer()
    meta = MediaMetadata(platform="generic", url="https://example.com/a.mp4", title="t")
    assert norm.enrich(meta) is meta


def test_storage_local_create():
    runtime = PluginRuntime(loader=PluginLoader())
    storage = runtime.create("mediacore-plugin-storage-local")
    assert storage.name == "local"
