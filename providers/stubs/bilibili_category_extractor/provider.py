"""Auto-generated MediaCore catalog stub for `bilibili_category_extractor`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class BilibiliCategoryExtractorProvider(StubProvider):
    name = 'bilibili_category_extractor'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('Bilibili category extractor',)
    source = "catalog"
    description = 'Catalog stub for bilibili_category_extractor'
