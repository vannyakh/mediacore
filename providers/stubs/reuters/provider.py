"""Auto-generated MediaCore catalog stub for `reuters`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class ReutersProvider(StubProvider):
    name = 'reuters'
    status = 'broken'
    host_suffixes = ()
    ie_names = ('Reuters',)
    source = "catalog"
    description = 'Catalog stub for reuters'
