"""Auto-generated MediaCore catalog stub for `geniuslyrics`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class GeniuslyricsProvider(StubProvider):
    name = 'geniuslyrics'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('GeniusLyrics',)
    source = "catalog"
    description = 'Catalog stub for geniuslyrics'
