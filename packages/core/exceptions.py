"""Domain exceptions for MediaCore."""


class MediaCoreError(Exception):
    def __init__(self, message: str, *, code: str = "mediacore_error") -> None:
        super().__init__(message)
        self.message = message
        self.code = code


class UnsupportedURLError(MediaCoreError):
    def __init__(self, url: str) -> None:
        super().__init__(f"No provider supports URL: {url}", code="unsupported_url")
        self.url = url


class InvalidURLError(MediaCoreError):
    def __init__(self, url: str, reason: str = "invalid URL") -> None:
        super().__init__(f"{reason}: {url}", code="invalid_url")
        self.url = url


class ProviderNotConfiguredError(MediaCoreError):
    def __init__(self, platform: str) -> None:
        super().__init__(
            f"Provider '{platform}' is not configured for permitted access",
            code="provider_not_configured",
        )
        self.platform = platform


class ProviderError(MediaCoreError):
    def __init__(self, platform: str, message: str) -> None:
        super().__init__(f"[{platform}] {message}", code="provider_error")
        self.platform = platform


class FormatNotFoundError(MediaCoreError):
    def __init__(self, format_id: str) -> None:
        super().__init__(f"Format not found: {format_id}", code="format_not_found")
        self.format_id = format_id


class DownloadError(MediaCoreError):
    def __init__(self, message: str) -> None:
        super().__init__(message, code="download_error")


class ValidationError(MediaCoreError):
    def __init__(self, message: str) -> None:
        super().__init__(message, code="validation_error")


class PluginError(MediaCoreError):
    def __init__(self, message: str) -> None:
        super().__init__(message, code="plugin_error")


class NotImplementedStageError(MediaCoreError):
    def __init__(self, stage: str) -> None:
        super().__init__(f"Pipeline stage not available: {stage}", code="stage_unavailable")
        self.stage = stage


# Back-compat alias used by older extractor shims
ExtractorError = MediaCoreError
