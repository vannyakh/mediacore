"""Auto-generated MediaCore catalog stub for `gaia`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class GaiaProvider(StubProvider):
    name = 'gaia'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('Gaia',)
    source = "catalog"
    description = 'Catalog stub for gaia'
