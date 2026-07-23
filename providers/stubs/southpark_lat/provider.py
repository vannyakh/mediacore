"""Auto-generated MediaCore catalog stub for `southpark.lat`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class SouthparkLatProvider(StubProvider):
    name = 'southpark.lat'
    status = 'not_configured'
    host_suffixes = ('southpark.lat',)
    ie_names = ('southpark.lat',)
    source = "catalog"
    description = 'Catalog stub for southpark.lat'
