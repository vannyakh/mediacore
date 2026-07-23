"""Auto-generated MediaCore catalog stub for `brightcove`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class BrightcoveProvider(StubProvider):
    name = 'brightcove'
    status = 'not_configured'
    host_suffixes = ('brightcove.com', 'players.brightcove.net')
    ie_names = ('brightcove:legacy', 'Brightcove', 'brightcove:new')
    source = "catalog"
    description = 'Catalog stub for brightcove'
