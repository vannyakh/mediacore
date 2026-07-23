"""Auto-generated MediaCore catalog stub for `tv2playseries.hu`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class Tv2playseriesHuProvider(StubProvider):
    name = 'tv2playseries.hu'
    status = 'not_configured'
    host_suffixes = ('tv2playseries.hu',)
    ie_names = ('tv2playseries.hu',)
    source = "catalog"
    description = 'Catalog stub for tv2playseries.hu'
