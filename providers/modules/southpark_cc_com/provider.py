"""Auto-generated MediaCore platform module for `southpark.cc.com`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class SouthparkCcComProvider(PlatformModule):
    name = 'southpark.cc.com'
    status = 'not_configured'
    host_suffixes = ('southpark.cc.com',)
    ie_names = ('southpark.cc.com', 'southpark.cc.com:español')
    source = "catalog"
    description = 'Platform module for southpark.cc.com'
