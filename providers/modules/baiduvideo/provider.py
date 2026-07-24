"""Auto-generated MediaCore platform module for `baiduvideo`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class BaiduvideoProvider(PlatformModule):
    name = 'baiduvideo'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('BaiduVideo',)
    source = "catalog"
    description = '百度视频'
