"""MediaCore Engine — orchestration over providers, pipeline, and events."""

from __future__ import annotations

from pathlib import Path

from packages.cache.memory import get_cache
from packages.core.downloader import set_progress_callback
from packages.core.models import DownloadResult, FormatInfo, LiveInfo, Manifest, MediaMetadata
from packages.core.pipeline import Pipeline, PipelineStage
from packages.core.validator import validate_format_id, validate_url
from packages.events.bus import EventType, get_event_bus
from packages.registry.providers import ProviderRegistry, get_registry


class MediaCoreEngine:
    def __init__(self, registry: ProviderRegistry | None = None) -> None:
        self.registry = registry or get_registry()
        self.events = get_event_bus()
        self.cache = get_cache()

    def analyze(
        self,
        url: str,
        *,
        allow_private: bool = False,
        job_id: str | None = None,
    ) -> MediaMetadata:
        url = validate_url(url, allow_private=allow_private)
        cache_key = f"analyze:{url}"
        cached = self.cache.get(cache_key)
        if isinstance(cached, MediaMetadata):
            return cached

        pipeline = Pipeline(url)
        pipeline.ctx.advance(PipelineStage.ANALYZE)
        self.events.emit(EventType.ANALYZE_STARTED, url=url, job_id=job_id)

        provider = self.registry.resolve(url)
        metadata = provider.get_metadata(url)
        if not metadata.formats:
            metadata.formats = provider.list_formats(url)
        if metadata.manifest is None:
            metadata.manifest = {
                "provider": metadata.platform,
                "formats": [f.id for f in metadata.formats],
            }

        pipeline.set_metadata(metadata.to_dict())
        self.events.emit(
            EventType.METADATA_READY,
            url=url,
            platform=metadata.platform,
            title=metadata.title,
            job_id=job_id,
        )
        self.cache.set(cache_key, metadata)
        return metadata

    def list_formats(self, url: str, *, allow_private: bool = False) -> list[FormatInfo]:
        url = validate_url(url, allow_private=allow_private)
        provider = self.registry.resolve(url)
        return provider.list_formats(url)

    def download(
        self,
        url: str,
        format_id: str,
        dest: Path,
        *,
        allow_private: bool = False,
        job_id: str | None = None,
    ) -> DownloadResult:
        url = validate_url(url, allow_private=allow_private)
        format_id = validate_format_id(format_id)
        self.events.emit(EventType.DOWNLOAD_STARTED, url=url, format=format_id, job_id=job_id)

        def _on_progress(bytes_done: int, bytes_total: int | None) -> None:
            percent: int | None
            if bytes_total and bytes_total > 0:
                percent = min(100, int(bytes_done * 100 / bytes_total))
            else:
                percent = None
            self.events.emit(
                EventType.PROGRESS,
                job_id=job_id,
                url=url,
                percent=percent,
                bytes_done=bytes_done,
                bytes_total=bytes_total,
            )

        set_progress_callback(_on_progress)
        try:
            _on_progress(0, None)
            provider = self.registry.resolve(url)
            result = provider.download(url, format_id, dest)
            self.events.emit(
                EventType.PROGRESS,
                job_id=job_id,
                url=url,
                percent=100,
                bytes_done=result.filesize,
                bytes_total=result.filesize,
            )
        finally:
            set_progress_callback(None)

        self.events.emit(
            EventType.COMPLETED,
            url=url,
            path=str(result.path),
            job_id=job_id,
        )
        return result

    def manifest(self, url: str, *, allow_private: bool = False) -> Manifest:
        url = validate_url(url, allow_private=allow_private)
        provider = self.registry.resolve(url)
        return provider.manifest(url)

    def thumbnail(self, url: str, *, allow_private: bool = False):
        url = validate_url(url, allow_private=allow_private)
        provider = self.registry.resolve(url)
        return provider.thumbnail(url)

    def subtitles(self, url: str, *, allow_private: bool = False):
        url = validate_url(url, allow_private=allow_private)
        provider = self.registry.resolve(url)
        return provider.subtitles(url)

    def live(self, url: str, *, allow_private: bool = False) -> LiveInfo | None:
        url = validate_url(url, allow_private=allow_private)
        provider = self.registry.resolve(url)
        return provider.live(url)

    def providers(self) -> list[dict[str, str]]:
        return self.registry.platforms()

    # Back-compat alias
    def platforms(self) -> list[dict[str, str]]:
        return self.providers()


# Back-compat
ExtractorEngine = MediaCoreEngine
