"""Auto-generated MediaCore catalog stub for `umg`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class UmgProvider(StubProvider):
    name = 'umg'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('umg:de',)
    source = "catalog"
    description = 'Universal Music Deutschland'
