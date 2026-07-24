"""Auto-generated MediaCore platform module for `vm.tiktok`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class VmTiktokProvider(PlatformModule):
    name = 'vm.tiktok'
    status = 'not_configured'
    host_suffixes = ('vm.tiktok',)
    ie_names = ('vm.tiktok',)
    source = "catalog"
    description = 'Platform module for vm.tiktok'
