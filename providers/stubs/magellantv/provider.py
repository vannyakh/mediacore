"""Auto-generated MediaCore catalog stub for `magellantv`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class MagellantvProvider(StubProvider):
    name = 'magellantv'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('MagellanTV',)
    source = "catalog"
    description = 'Catalog stub for magellantv'
