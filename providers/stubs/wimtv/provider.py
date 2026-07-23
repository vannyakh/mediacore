"""Auto-generated MediaCore catalog stub for `wimtv`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class WimtvProvider(StubProvider):
    name = 'wimtv'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('WimTV',)
    source = "catalog"
    description = 'Catalog stub for wimtv'
