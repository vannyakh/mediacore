"""Auto-generated MediaCore platform module for `video.sky.it`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class VideoSkyItProvider(PlatformModule):
    name = 'video.sky.it'
    status = 'not_configured'
    host_suffixes = ('video.sky.it',)
    ie_names = ('video.sky.it', 'video.sky.it:live')
    source = "catalog"
    description = 'Platform module for video.sky.it'
