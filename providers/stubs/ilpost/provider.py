"""Auto-generated MediaCore catalog stub for `ilpost`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class IlpostProvider(StubProvider):
    name = 'ilpost'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('IlPost',)
    source = "catalog"
    description = 'Catalog stub for ilpost'
