"""Shared direct-media metadata/download helpers for platform modules and generic."""

from __future__ import annotations

from pathlib import Path
from urllib.parse import unquote, urlparse

from packages.core.downloader import download_file, head_content_type
from packages.core.exceptions import FormatNotFoundError, ProviderError
from packages.core.models import DownloadResult, FormatInfo, Manifest, MediaMetadata
from packages.core.parser import extension_from_url, is_direct_media_url, is_stream_playlist_url


def direct_metadata(platform: str, url: str) -> MediaMetadata:
    filename = unquote(urlparse(url).path.rsplit("/", 1)[-1] or "media")
    content_type = head_content_type(url)
    ext = extension_from_url(url, default="mp4")
    stream = is_stream_playlist_url(url) or (
        bool(content_type)
        and ("mpegurl" in content_type.lower() or "dash+xml" in content_type.lower())
    )
    if stream and ext in {"m3u8", "mpd", "bin"}:
        ext = "mp4"
    fmt = FormatInfo(
        id="original",
        quality="original",
        container=ext,
        mime_type=content_type,
        url=url,
    )
    manifest = Manifest(
        type="hls" if stream else "direct",
        provider=platform,
        url=url,
        format_ids=[fmt.id],
        extra={"stream": stream} if stream else {},
    )
    return MediaMetadata(
        platform=platform,
        url=url,
        title=filename,
        formats=[fmt],
        manifest=manifest,
    )


def direct_download(
    platform: str,
    url: str,
    format_id: str,
    dest: Path,
) -> DownloadResult:
    if not is_direct_media_url(url):
        raise ProviderError(
            platform,
            "URL is not a direct media or stream playlist (.mp4/.m3u8/…)",
        )
    meta = direct_metadata(platform, url)
    fmt = next((f for f in meta.formats if f.id == format_id or f.quality == format_id), None)
    if fmt is None:
        raise FormatNotFoundError(format_id)
    if not fmt.url:
        raise ProviderError(platform, "No downloadable URL for format")
    container = fmt.container if fmt.container not in {"m3u8", "mpd"} else "mp4"
    target = dest if dest.suffix else dest.with_suffix(f".{container}")
    size, content_type = download_file(fmt.url, target)
    return DownloadResult(
        path=target,
        format_id=fmt.id,
        container=container,
        filesize=size,
        content_type=content_type or fmt.mime_type,
    )
