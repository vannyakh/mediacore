"""Auto-generated MediaCore catalog stub for `7plus`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class P7plusProvider(StubProvider):
    name = '7plus'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('7plus',)
    source = "catalog"
    description = 'Catalog stub for 7plus'
