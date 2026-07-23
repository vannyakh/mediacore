"""Auto-generated MediaCore catalog stub for `toutiao`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class ToutiaoProvider(StubProvider):
    name = 'toutiao'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('toutiao',)
    source = "catalog"
    description = '今日头条'
