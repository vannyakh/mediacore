"""Default format selection for analyze/download."""

from __future__ import annotations

from packages.core.exceptions import FormatNotFoundError
from packages.core.models import FormatInfo

_DEFAULT_FORMAT_ALIASES = frozenset({"", "original", "best", "default"})


def select_format_id(formats: list[FormatInfo], format_id: str | None) -> str:
    """Pick a format id: explicit match, else sole format, else preferred container."""
    if not formats:
        raise FormatNotFoundError(format_id or "original")
    requested = (format_id or "original").strip()
    ids = {f.id for f in formats}
    if requested not in _DEFAULT_FORMAT_ALIASES:
        if requested in ids:
            return requested
        raise FormatNotFoundError(requested)
    if len(formats) == 1:
        return formats[0].id
    preferred = ("mp4", "webm", "mp3", "m4a", "mkv")
    for container in preferred:
        for fmt in formats:
            if (fmt.container or "").lower() == container:
                return fmt.id
    return formats[0].id
