"""Auto-generated MediaCore catalog stub for `prxseries`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class PrxseriesProvider(StubProvider):
    name = 'prxseries'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('PRXSeries', 'prxseries:search')
    source = "catalog"
    description = 'PRX Series Search; "prxseries:" prefix'
