"""Auto-generated MediaCore catalog stub for `xiaohongshu`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class XiaohongshuProvider(StubProvider):
    name = 'xiaohongshu'
    status = 'not_configured'
    host_suffixes = ('xiaohongshu.com', 'www.xiaohongshu.com', 'xhslink.com')
    ie_names = ('XiaoHongShu',)
    source = "catalog"
    description = '小红书'
