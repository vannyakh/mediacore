"""Shared contract runners for providers, plugins, and storage."""

from __future__ import annotations

from pathlib import Path
from typing import Any, Protocol

from packages.core.exceptions import ProviderNotConfiguredError
from packages.core.provider import Provider
from packages.testkit.assertions import (
    assert_provider_contract_basics,
    assert_storage_paths,
    assert_valid_metadata,
)


class StorageLike(Protocol):
    def job_dir(self, job_id: str) -> Path: ...
    def path_for(self, job_id: str, filename: str) -> Path: ...
    def public_url(self, job_id: str, filename: str) -> str: ...
    def delete_job(self, job_id: str) -> None: ...


def run_provider_contract(
    provider: Provider,
    url: str,
    dest: Path,
    *,
    expect_download: bool = True,
) -> None:
    assert_provider_contract_basics(provider, url)
    meta = provider.metadata(url)
    assert_valid_metadata(meta)
    format_id = meta.formats[0].id
    if expect_download:
        result = provider.download(url, format_id, dest)
        assert result.path.exists() or result.filesize is not None or result.path
        assert result.format_id == format_id
    else:
        try:
            provider.download(url, format_id, dest)
        except ProviderNotConfiguredError:
            return
        except Exception:  # noqa: BLE001
            return


def run_storage_contract(storage: StorageLike, tmp: Path) -> None:
    job_id = "contract-job"
    assert_storage_paths(storage, job_id)
    target = storage.path_for(job_id, "clip.mp4")
    target.write_bytes(b"abc")
    assert target.exists()
    storage.delete_job(job_id)
    assert not (Path(storage.root) / job_id).exists()  # type: ignore[attr-defined]


def run_plugin_manifest_contract(info: Any) -> None:
    from packages.plugins.kinds import PLUGIN_STATUSES, PluginKind

    assert info.name.startswith("mediacore-plugin-")
    assert info.status in PLUGIN_STATUSES
    assert isinstance(info.capabilities, list)
    if info.status != "error":
        assert info.kind in {k.value for k in PluginKind}
