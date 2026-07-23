"""Auto-generated MediaCore catalog stub for `tiktok`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class TiktokProvider(StubProvider):
    name = 'tiktok'
    status = 'broken'
    host_suffixes = ('tiktok.com', 'www.tiktok.com', 'vm.tiktok.com', 'm.tiktok.com')
    ie_names = ('TikTok', 'tiktok', 'tiktok:collection', 'tiktok:effect', 'tiktok:live', 'tiktok:sound', 'tiktok:tag', 'tiktok:user')
    source = "catalog"
    description = 'Catalog stub for tiktok'
