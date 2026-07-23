"""Auto-generated MediaCore catalog stub for `vids.io`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class VidsIoProvider(StubProvider):
    name = 'vids.io'
    status = 'not_configured'
    host_suffixes = ('vids.io',)
    ie_names = ('vids.io',)
    source = "catalog"
    description = 'Catalog stub for vids.io'
