"""Auto-generated MediaCore catalog stub for `s4c`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class S4cProvider(StubProvider):
    name = 's4c'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('S4C',)
    source = "catalog"
    description = 'Catalog stub for s4c'
