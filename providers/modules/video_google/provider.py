"""Auto-generated MediaCore platform module for `video.google`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class VideoGoogleProvider(PlatformModule):
    name = 'video.google'
    status = 'not_configured'
    host_suffixes = ('video.google',)
    ie_names = ('video.google:search',)
    source = "catalog"
    description = 'Google Video search; "gvsearch:" prefix'
