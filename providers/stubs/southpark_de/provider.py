"""Auto-generated MediaCore catalog stub for `southpark.de`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class SouthparkDeProvider(StubProvider):
    name = 'southpark.de'
    status = 'not_configured'
    host_suffixes = ('southpark.de',)
    ie_names = ('southpark.de',)
    source = "catalog"
    description = 'Catalog stub for southpark.de'
