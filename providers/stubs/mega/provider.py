"""Auto-generated MediaCore catalog stub for `mega`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class MegaProvider(StubProvider):
    name = 'mega'
    status = 'not_configured'
    host_suffixes = ('mega.nz', 'mega.co.nz')
    ie_names = ('MEGA',)
    source = "catalog"
    description = 'Catalog stub for mega'
