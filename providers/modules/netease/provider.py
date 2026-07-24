"""Auto-generated MediaCore platform module for `netease`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class NeteaseProvider(PlatformModule):
    name = 'netease'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('netease:album', 'netease:djradio', 'netease:mv', 'netease:playlist', 'netease:program', 'netease:singer', 'netease:song')
    source = "catalog"
    description = '网易云音乐 - 专辑'
