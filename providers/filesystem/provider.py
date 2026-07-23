"""Filesystem provider for local file:// URLs and absolute paths."""

from __future__ import annotations

import shutil
from pathlib import Path
from urllib.parse import unquote, urlparse

from packages.core.exceptions import FormatNotFoundError, ProviderError
from packages.core.models import (
    DownloadResult,
    FormatInfo,
    Manifest,
    MediaMetadata,
    ProviderCapabilities,
)
from packages.core.provider import Provider


class FilesystemProvider(Provider):
    name = "filesystem"
    status = "active"
    capabilities = ProviderCapabilities(
        metadata=True,
        manifest=True,
        formats=True,
        download=True,
        thumbnail=False,
        subtitle=False,
        live=False,
    )

    def supports(self, url: str) -> bool:
        if url.startswith("file://"):
            return True
        path = Path(url)
        return path.is_absolute() and path.exists() and path.is_file()

    def _resolve(self, url: str) -> Path:
        if url.startswith("file://"):
            parsed = urlparse(url)
            return Path(unquote(parsed.path))
        return Path(url)

    def metadata(self, url: str) -> MediaMetadata:
        path = self._resolve(url)
        if not path.exists():
            raise ProviderError(self.name, f"File not found: {path}")
        ext = path.suffix.lstrip(".") or "bin"
        fmt = FormatInfo(
            id="original",
            quality="original",
            container=ext,
            filesize=path.stat().st_size,
            url=path.as_uri(),
        )
        manifest = Manifest(
            type="filesystem",
            provider=self.name,
            url=path.as_uri(),
            format_ids=[fmt.id],
            extra={"path": str(path)},
        )
        return MediaMetadata(
            platform=self.name,
            url=path.as_uri(),
            title=path.name,
            formats=[fmt],
            manifest=manifest,
        )

    def formats(self, url: str) -> list[FormatInfo]:
        return self.metadata(url).formats

    def download(self, url: str, format_id: str, dest: Path) -> DownloadResult:
        meta = self.metadata(url)
        fmt = next((f for f in meta.formats if f.id == format_id or f.quality == format_id), None)
        if fmt is None:
            raise FormatNotFoundError(format_id)
        source = self._resolve(url)
        target = dest if dest.suffix else dest.with_suffix(source.suffix)
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)
        return DownloadResult(
            path=target,
            format_id=fmt.id,
            container=fmt.container,
            filesize=target.stat().st_size,
        )
