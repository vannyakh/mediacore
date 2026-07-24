"""Auto-generated MediaCore platform module for `youpornvideos`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class YoupornvideosProvider(PlatformModule):
    name = 'youpornvideos'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('YouPornVideos',)
    source = "catalog"
    description = 'YouPorn video (browse) playlists, with sorting, filtering and pagination'
