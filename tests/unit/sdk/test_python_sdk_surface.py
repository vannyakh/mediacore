"""Ensure Python SDK exposes the unified MediaCore surface."""

from pathlib import Path

import pytest

pytestmark = pytest.mark.unit


def test_python_sdk_has_unified_api():
    import sys

    root = Path(__file__).resolve().parents[3] / "sdk" / "python"
    sys.path.insert(0, str(root))
    from mediacore_sdk import MediaCore

    client = MediaCore("test-key", base_url="http://127.0.0.1:9")
    assert hasattr(client.media, "analyze")
    assert hasattr(client.media, "download")
    assert hasattr(client.media, "convert")
    assert hasattr(client.media, "thumbnail")
    assert hasattr(client.jobs, "list")
    assert hasattr(client.jobs, "get")
    assert hasattr(client.plugins, "list")
    client.close()
