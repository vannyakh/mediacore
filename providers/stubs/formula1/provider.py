"""Auto-generated MediaCore catalog stub for `formula1`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class Formula1Provider(StubProvider):
    name = 'formula1'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('Formula1',)
    source = "catalog"
    description = 'Catalog stub for formula1'
