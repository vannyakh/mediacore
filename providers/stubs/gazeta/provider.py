"""Auto-generated MediaCore catalog stub for `gazeta`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class GazetaProvider(StubProvider):
    name = 'gazeta'
    status = 'broken'
    host_suffixes = ()
    ie_names = ('Gazeta',)
    source = "catalog"
    description = 'Catalog stub for gazeta'
