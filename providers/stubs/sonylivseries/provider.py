"""Auto-generated MediaCore catalog stub for `sonylivseries`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class SonylivseriesProvider(StubProvider):
    name = 'sonylivseries'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('SonyLIVSeries',)
    source = "catalog"
    description = 'Catalog stub for sonylivseries'
