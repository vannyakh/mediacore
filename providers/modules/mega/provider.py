"""Auto-generated MediaCore platform module for `mega`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class MegaProvider(PlatformModule):
    name = 'mega'
    status = 'not_configured'
    host_suffixes = ('mega.nz', 'mega.co.nz')
    ie_names = ('MEGA',)
    source = "catalog"
    description = 'Platform module for mega'
