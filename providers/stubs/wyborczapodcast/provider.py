"""Auto-generated MediaCore catalog stub for `wyborczapodcast`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class WyborczapodcastProvider(StubProvider):
    name = 'wyborczapodcast'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('WyborczaPodcast',)
    source = "catalog"
    description = 'Catalog stub for wyborczapodcast'
