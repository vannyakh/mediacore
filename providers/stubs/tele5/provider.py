"""Auto-generated MediaCore catalog stub for `tele5`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class Tele5Provider(StubProvider):
    name = 'tele5'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('Tele5',)
    source = "catalog"
    description = 'Catalog stub for tele5'
