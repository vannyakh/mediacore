"""Auto-generated MediaCore platform module for `phoenix.de`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class PhoenixDeProvider(PlatformModule):
    name = 'phoenix.de'
    status = 'not_configured'
    host_suffixes = ('phoenix.de',)
    ie_names = ('phoenix.de',)
    source = "catalog"
    description = 'Platform module for phoenix.de'
