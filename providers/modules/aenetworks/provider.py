"""Auto-generated MediaCore platform module for `aenetworks`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class AenetworksProvider(PlatformModule):
    name = 'aenetworks'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('aenetworks', 'aenetworks:collection', 'aenetworks:show')
    source = "catalog"
    description = 'A+E Networks: A&E, Lifetime, History.com, FYI Network and History Vault'
