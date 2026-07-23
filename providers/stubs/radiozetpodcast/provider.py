"""Auto-generated MediaCore catalog stub for `radiozetpodcast`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class RadiozetpodcastProvider(StubProvider):
    name = 'radiozetpodcast'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('RadioZetPodcast',)
    source = "catalog"
    description = 'Catalog stub for radiozetpodcast'
