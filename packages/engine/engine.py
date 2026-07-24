"""MediaCore Engine — orchestration over providers, pipeline, and events."""

from __future__ import annotations

from pathlib import Path

from packages.cache.memory import get_cache
from packages.core.downloader import set_progress_callback
from packages.core.exceptions import FormatNotFoundError, ProviderNotConfiguredError
from packages.core.format_select import select_format_id
from packages.core.models import DownloadResult, FormatInfo, LiveInfo, Manifest, MediaMetadata
from packages.core.pipeline import Pipeline, PipelineStage
from packages.core.validator import validate_format_id, validate_url
from packages.events.bus import EventType, get_event_bus
from packages.registry.providers import ProviderRegistry, get_registry

# Re-export for callers/tests
__all__ = ["ExtractorEngine", "MediaCoreEngine", "select_format_id"]


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
        pipeline.ctx.advance(PipelineStage.METADATA)

        if not metadata.formats:
            metadata.formats = provider.list_formats(url)
        pipeline.ctx.advance(PipelineStage.FORMATS)
        pipeline.ctx.formats = [f.to_dict() for f in metadata.formats]

        if metadata.manifest is None:
            metadata.manifest = {
                "provider": metadata.platform,
                "formats": [f.id for f in metadata.formats],
            }
        pipeline.ctx.advance(PipelineStage.MANIFEST)

        try:
            from packages.plugins.runtime import get_runtime

            metadata = get_runtime().metadata_normalizer().enrich(metadata)
        except Exception:  # noqa: BLE001
            pass

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
        pipeline = Pipeline(url)
        pipeline.ctx.advance(PipelineStage.ANALYZE)

        provider = self.registry.resolve(url)
        if getattr(provider, "status", "active") == "metadata_only" and not getattr(
            provider.capabilities, "download", True
        ):
            raise ProviderNotConfiguredError(
                f"{provider.name} (metadata only — use analyze/-s; "
                "download needs a direct media, share-link, or permitted API source)"
            )

        formats = provider.list_formats(url)
        pipeline.ctx.advance(PipelineStage.FORMATS)
        chosen = select_format_id(formats, format_id)
        pipeline.ctx.advance(PipelineStage.DOWNLOAD)

        self.events.emit(EventType.DOWNLOAD_STARTED, url=url, format=chosen, job_id=job_id)

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
            result = provider.download(url, chosen, dest)
            pipeline.ctx.artifact_path = str(result.path)
            pipeline.ctx.advance(PipelineStage.EXPORT)
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

    def process(
        self,
        source: Path,
        dest: Path,
        *,
        step: str = "remux",
        audio_codec: str = "mp3",
        job_id: str | None = None,
    ) -> Path:
        """Postprocess an already-downloaded file (remux / extract_audio)."""
        from packages.core.postprocess import PostprocessRequest, PostprocessStep, run_postprocess

        pipeline = Pipeline(str(source))
        pipeline.ctx.advance(PipelineStage.PROCESSING)
        try:
            pp_step = PostprocessStep(step)
        except ValueError as exc:
            raise FormatNotFoundError(step) from exc
        path = run_postprocess(
            PostprocessRequest(
                source=source,
                dest=dest,
                step=pp_step,
                audio_codec=audio_codec,
            )
        )
        pipeline.ctx.artifact_path = str(path)
        pipeline.ctx.advance(PipelineStage.EXPORT)
        self.events.emit(
            EventType.COMPLETED,
            url=str(source),
            path=str(path),
            job_id=job_id,
            step=step,
        )
        return path

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
