"""Auto-generated MediaCore catalog stub for `4tube`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class P4tubeProvider(StubProvider):
    name = '4tube'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('4tube',)
    source = "catalog"
    description = 'Catalog stub for 4tube'
