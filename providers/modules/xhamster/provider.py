"""Auto-generated MediaCore platform module for `xhamster`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class XhamsterProvider(PlatformModule):
    name = 'xhamster'
    status = 'not_configured'
    host_suffixes = ('xhamster.com', 'www.xhamster.com')
    ie_names = ('XHamster',)
    source = "catalog"
    description = 'Platform module for xhamster'
