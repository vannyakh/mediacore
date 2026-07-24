"""Auto-generated MediaCore platform module for `24tv.ua`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class P24tvUaProvider(PlatformModule):
    name = '24tv.ua'
    status = 'not_configured'
    host_suffixes = ('24tv.ua',)
    ie_names = ('24tv.ua',)
    source = "catalog"
    description = 'Platform module for 24tv.ua'
