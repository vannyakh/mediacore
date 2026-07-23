"""Auto-generated MediaCore catalog stub for `folketinget`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class FolketingetProvider(StubProvider):
    name = 'folketinget'
    status = 'broken'
    host_suffixes = ()
    ie_names = ('Folketinget',)
    source = "catalog"
    description = 'Folketinget (ft.dk; Danish parliament)'
