"""Shared assertion helpers for contract and API tests."""

from __future__ import annotations

from typing import Any

from packages.core.models import MediaMetadata
from packages.core.provider import Provider


def assert_valid_metadata(meta: MediaMetadata) -> None:
    assert meta.platform
    assert meta.url
    assert meta.title
    assert isinstance(meta.formats, list)
    for fmt in meta.formats:
        assert fmt.id
        assert fmt.container


def assert_provider_contract_basics(provider: Provider, url: str) -> None:
    assert provider.supports(url) is True
    meta = provider.metadata(url)
    assert_valid_metadata(meta)
    formats = provider.formats(url)
    assert formats
    assert all(f.id for f in formats)
    caps = getattr(provider, "capabilities", None)
    if caps is not None:
        assert caps.metadata is True
        assert "metadata" in caps.to_list()


def assert_storage_paths(storage: Any, job_id: str = "job-1") -> None:
    d = storage.job_dir(job_id)
    assert d.exists()
    p = storage.path_for(job_id, "out.mp4")
    assert p.name == "out.mp4"
    assert storage.public_url(job_id, "out.mp4") == f"/files/{job_id}/out.mp4"
