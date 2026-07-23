"""Auto-generated MediaCore catalog stub for `bilibili`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class BilibiliProvider(StubProvider):
    name = 'bilibili'
    status = 'not_configured'
    host_suffixes = ('bilibili.com', 'www.bilibili.com', 'b23.tv', 'space.bilibili.com')
    ie_names = ('BiliBili', 'Bilibili')
    source = "catalog"
    description = 'Catalog stub for bilibili'
