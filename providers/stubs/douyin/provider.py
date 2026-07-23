"""Auto-generated MediaCore catalog stub for `douyin`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class DouyinProvider(StubProvider):
    name = 'douyin'
    status = 'not_configured'
    host_suffixes = ('douyin.com', 'www.douyin.com', 'v.douyin.com')
    ie_names = ('Douyin',)
    source = "catalog"
    description = 'Catalog stub for douyin'
