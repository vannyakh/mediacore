"""Auto-generated MediaCore catalog stub for `tv.dfb.de`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class TvDfbDeProvider(StubProvider):
    name = 'tv.dfb.de'
    status = 'not_configured'
    host_suffixes = ('tv.dfb.de',)
    ie_names = ('tv.dfb.de',)
    source = "catalog"
    description = 'Catalog stub for tv.dfb.de'
