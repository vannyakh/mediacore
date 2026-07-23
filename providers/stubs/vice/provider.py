"""Auto-generated MediaCore catalog stub for `vice`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class ViceProvider(StubProvider):
    name = 'vice'
    status = 'broken'
    host_suffixes = ()
    ie_names = ('vice', 'vice:article', 'vice:show')
    source = "catalog"
    description = 'Catalog stub for vice'
