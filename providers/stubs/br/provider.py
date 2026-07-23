"""Auto-generated MediaCore catalog stub for `br`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class BrProvider(StubProvider):
    name = 'br'
    status = 'broken'
    host_suffixes = ()
    ie_names = ('BR',)
    source = "catalog"
    description = 'Bayerischer Rundfunk'
