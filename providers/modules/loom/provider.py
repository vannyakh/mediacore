"""Auto-generated MediaCore platform module for `loom`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class LoomProvider(PlatformModule):
    name = 'loom'
    status = 'broken'
    host_suffixes = ('loom.com', 'www.loom.com')
    ie_names = ('loom', 'Loom', 'loom:folder')
    source = "catalog"
    description = 'Platform module for loom'
