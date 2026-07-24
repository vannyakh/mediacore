"""Auto-generated MediaCore platform module for `pinterest`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class PinterestProvider(PlatformModule):
    name = 'pinterest'
    status = 'not_configured'
    host_suffixes = ('pinterest.com', 'www.pinterest.com', 'pin.it')
    ie_names = ('Pinterest',)
    source = "catalog"
    description = 'Platform module for pinterest'
