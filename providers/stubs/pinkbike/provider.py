"""Auto-generated MediaCore catalog stub for `pinkbike`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class PinkbikeProvider(StubProvider):
    name = 'pinkbike'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('Pinkbike',)
    source = "catalog"
    description = 'Catalog stub for pinkbike'
