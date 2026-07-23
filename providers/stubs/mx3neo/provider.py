"""Auto-generated MediaCore catalog stub for `mx3neo`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class Mx3neoProvider(StubProvider):
    name = 'mx3neo'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('Mx3Neo',)
    source = "catalog"
    description = 'Catalog stub for mx3neo'
