"""Auto-generated MediaCore catalog stub for `video.sky.it`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class VideoSkyItProvider(StubProvider):
    name = 'video.sky.it'
    status = 'not_configured'
    host_suffixes = ('video.sky.it',)
    ie_names = ('video.sky.it', 'video.sky.it:live')
    source = "catalog"
    description = 'Catalog stub for video.sky.it'
