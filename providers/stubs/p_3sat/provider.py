"""Auto-generated MediaCore catalog stub for `3sat`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class P3satProvider(StubProvider):
    name = '3sat'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('3sat',)
    source = "catalog"
    description = 'Catalog stub for 3sat'
