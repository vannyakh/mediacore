"""Auto-generated MediaCore catalog stub for `thesun`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class ThesunProvider(StubProvider):
    name = 'thesun'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('TheSun',)
    source = "catalog"
    description = 'Catalog stub for thesun'
