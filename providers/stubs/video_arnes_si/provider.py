"""Auto-generated MediaCore catalog stub for `video.arnes.si`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class VideoArnesSiProvider(StubProvider):
    name = 'video.arnes.si'
    status = 'not_configured'
    host_suffixes = ('video.arnes.si',)
    ie_names = ('video.arnes.si',)
    source = "catalog"
    description = 'Arnes Video'
