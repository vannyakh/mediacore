"""Auto-generated MediaCore platform module for `video.arnes.si`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class VideoArnesSiProvider(PlatformModule):
    name = 'video.arnes.si'
    status = 'not_configured'
    host_suffixes = ('video.arnes.si',)
    ie_names = ('video.arnes.si',)
    source = "catalog"
    description = 'Arnes Video'
