"""Auto-generated MediaCore platform module for `nbcnews`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class NbcnewsProvider(PlatformModule):
    name = 'nbcnews'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('NBCNews',)
    source = "catalog"
    description = 'Platform module for nbcnews'
