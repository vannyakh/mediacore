"""Auto-generated MediaCore platform module for `iqiyi`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class IqiyiProvider(PlatformModule):
    name = 'iqiyi'
    status = 'not_configured'
    host_suffixes = ('iqiyi.com', 'www.iqiyi.com')
    ie_names = ('iqiyi',)
    source = "catalog"
    description = '爱奇艺'
