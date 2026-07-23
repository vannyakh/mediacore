"""MediaCore Engine — orchestration over providers, pipeline, and events."""

from __future__ import annotations

from pathlib import Path

from packages.cache.memory import get_cache
from packages.core.models import DownloadResult, FormatInfo, MediaMetadata
from packages.core.pipeline import Pipeline, PipelineStage
from packages.core.validator import validate_format_id, validate_url
from packages.events.bus import EventType, get_event_bus
from packages.registry.providers import ProviderRegistry, get_registry


class MediaCoreEngine:
    def __init__(self, registry: ProviderRegistry | None = None) -> None:
        self.registry = registry or get_registry()
        self.events = get_event_bus()
        self.cache = get_cache()

    def analyze(self, url: str, *, allow_private: bool = False) -> MediaMetadata:
        url = validate_url(url, allow_private=allow_private)
        cache_key = f"analyze:{url}"
        cached = self.cache.get(cache_key)
        if isinstance(cached, MediaMetadata):
            return cached

        pipeline = Pipeline(url)
        pipeline.ctx.advance(PipelineStage.ANALYZE)
        self.events.emit(EventType.ANALYZE_STARTED, url=url)

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
        provider = self.registry.resolve(url)
        result = provider.download(url, format_id, dest)
        self.events.emit(
            EventType.COMPLETED,
            url=url,
            path=str(result.path),
            job_id=job_id,
        )
        return result

    def thumbnail(self, url: str, *, allow_private: bool = False) -> str | None:
        url = validate_url(url, allow_private=allow_private)
        provider = self.registry.resolve(url)
        return provider.thumbnail(url)

    def subtitles(self, url: str, *, allow_private: bool = False) -> list[dict]:
        url = validate_url(url, allow_private=allow_private)
        provider = self.registry.resolve(url)
        return provider.subtitles(url)

    def providers(self) -> list[dict[str, str]]:
        return self.registry.platforms()

    # Back-compat alias
    def platforms(self) -> list[dict[str, str]]:
        return self.providers()


# Back-compat
ExtractorEngine = MediaCoreEngine
