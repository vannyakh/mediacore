"""Auto-generated MediaCore catalog stub for `video.google`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class VideoGoogleProvider(StubProvider):
    name = 'video.google'
    status = 'not_configured'
    host_suffixes = ('video.google',)
    ie_names = ('video.google:search',)
    source = "catalog"
    description = 'Google Video search; "gvsearch:" prefix'
