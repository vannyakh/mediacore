"""Auto-generated MediaCore catalog stub for `nebula`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class NebulaProvider(StubProvider):
    name = 'nebula'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('nebula:channel', 'nebula:media', 'nebula:season', 'nebula:subscriptions', 'nebula:video')
    source = "catalog"
    description = 'Catalog stub for nebula'
