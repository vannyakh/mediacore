"""Auto-generated MediaCore catalog stub for `biography`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class BiographyProvider(StubProvider):
    name = 'biography'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('Biography',)
    source = "catalog"
    description = 'Catalog stub for biography'
