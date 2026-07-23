"""Auto-generated MediaCore catalog stub for `radlive`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class RadliveProvider(StubProvider):
    name = 'radlive'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('radlive', 'radlive:channel', 'radlive:season')
    source = "catalog"
    description = 'Catalog stub for radlive'
