"""Auto-generated MediaCore catalog stub for `plutotv`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class PlutotvProvider(StubProvider):
    name = 'plutotv'
    status = 'broken'
    host_suffixes = ()
    ie_names = ('PlutoTV',)
    source = "catalog"
    description = 'Catalog stub for plutotv'
