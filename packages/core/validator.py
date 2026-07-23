"""URL and request validation."""

from __future__ import annotations

from urllib.parse import urlparse

from packages.core.exceptions import InvalidURLError, ValidationError

BLOCKED_HOSTS = {
    "localhost",
    "127.0.0.1",
    "0.0.0.0",
    "::1",
    "metadata.google.internal",
}


def validate_url(url: str, *, allow_private: bool = False) -> str:
    if not url or not isinstance(url, str):
        raise InvalidURLError(str(url), "URL is required")

    url = url.strip()
    parsed = urlparse(url)
    if parsed.scheme not in {"http", "https", "file"}:
        raise InvalidURLError(url, "Only http/https/file URLs are allowed")
    if parsed.scheme != "file" and not parsed.netloc:
        raise InvalidURLError(url, "URL must include a host")

    host = (parsed.hostname or "").lower()
    if parsed.scheme != "file" and not allow_private and host in BLOCKED_HOSTS:
        raise InvalidURLError(url, "Private/local hosts are not allowed")
    if not allow_private and host.startswith("169.254."):
        raise InvalidURLError(url, "Link-local addresses are not allowed")

    return url


def validate_format_id(format_id: str | None) -> str:
    if not format_id or not str(format_id).strip():
        raise ValidationError("format is required")
    return str(format_id).strip()
