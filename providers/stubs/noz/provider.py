"""Auto-generated MediaCore catalog stub for `noz`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class NozProvider(StubProvider):
    name = 'noz'
    status = 'broken'
    host_suffixes = ()
    ie_names = ('Noz',)
    source = "catalog"
    description = 'Catalog stub for noz'
