"""Auto-generated MediaCore catalog stub for `loco`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class LocoProvider(StubProvider):
    name = 'loco'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('Loco',)
    source = "catalog"
    description = 'Catalog stub for loco'
