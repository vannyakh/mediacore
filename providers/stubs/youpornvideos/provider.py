"""Auto-generated MediaCore catalog stub for `youpornvideos`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class YoupornvideosProvider(StubProvider):
    name = 'youpornvideos'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('YouPornVideos',)
    source = "catalog"
    description = 'YouPorn video (browse) playlists, with sorting, filtering and pagination'
