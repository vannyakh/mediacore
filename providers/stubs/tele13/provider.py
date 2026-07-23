"""Auto-generated MediaCore catalog stub for `tele13`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class Tele13Provider(StubProvider):
    name = 'tele13'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('Tele13',)
    source = "catalog"
    description = 'Catalog stub for tele13'
