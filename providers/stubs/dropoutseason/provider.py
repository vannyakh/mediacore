"""Auto-generated MediaCore catalog stub for `dropoutseason`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class DropoutseasonProvider(StubProvider):
    name = 'dropoutseason'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('DropoutSeason',)
    source = "catalog"
    description = 'Catalog stub for dropoutseason'
