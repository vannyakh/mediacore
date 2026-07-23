"""Auto-generated MediaCore catalog stub for `netease`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class NeteaseProvider(StubProvider):
    name = 'netease'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('netease:album', 'netease:djradio', 'netease:mv', 'netease:playlist', 'netease:program', 'netease:singer', 'netease:song')
    source = "catalog"
    description = '网易云音乐 - 专辑'
