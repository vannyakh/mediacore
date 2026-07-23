"""Auto-generated MediaCore catalog stub for `bilibilisearch`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class BilibilisearchProvider(StubProvider):
    name = 'bilibilisearch'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('BiliBiliSearch',)
    source = "catalog"
    description = 'Bilibili video search; "bilisearch:" prefix'
