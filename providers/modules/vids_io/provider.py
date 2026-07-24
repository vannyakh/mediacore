"""Auto-generated MediaCore platform module for `vids.io`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class VidsIoProvider(PlatformModule):
    name = 'vids.io'
    status = 'not_configured'
    host_suffixes = ('vids.io',)
    ie_names = ('vids.io',)
    source = "catalog"
    description = 'Platform module for vids.io'
