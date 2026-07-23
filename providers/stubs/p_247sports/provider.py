"""Auto-generated MediaCore catalog stub for `247sports`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class P247sportsProvider(StubProvider):
    name = '247sports'
    status = 'broken'
    host_suffixes = ()
    ie_names = ('247sports',)
    source = "catalog"
    description = 'Catalog stub for 247sports'
