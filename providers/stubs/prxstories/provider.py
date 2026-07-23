"""Auto-generated MediaCore catalog stub for `prxstories`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class PrxstoriesProvider(StubProvider):
    name = 'prxstories'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('prxstories:search',)
    source = "catalog"
    description = 'PRX Stories Search; "prxstories:" prefix'
