"""Auto-generated MediaCore catalog stub for `pialive`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class PialiveProvider(StubProvider):
    name = 'pialive'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('PiaLive',)
    source = "catalog"
    description = 'Catalog stub for pialive'
