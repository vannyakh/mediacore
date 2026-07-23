"""Auto-generated MediaCore catalog stub for `goodgame`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class GoodgameProvider(StubProvider):
    name = 'goodgame'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('goodgame:stream',)
    source = "catalog"
    description = 'Catalog stub for goodgame'
