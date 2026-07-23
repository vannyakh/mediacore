"""Auto-generated MediaCore catalog stub for `cp24`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class Cp24Provider(StubProvider):
    name = 'cp24'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('cp24',)
    source = "catalog"
    description = 'Catalog stub for cp24'
