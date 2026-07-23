"""Auto-generated MediaCore catalog stub for `aenetworks`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class AenetworksProvider(StubProvider):
    name = 'aenetworks'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('aenetworks', 'aenetworks:collection', 'aenetworks:show')
    source = "catalog"
    description = 'A+E Networks: A&E, Lifetime, History.com, FYI Network and History Vault'
