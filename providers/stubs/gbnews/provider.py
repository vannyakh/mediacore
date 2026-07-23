"""Auto-generated MediaCore catalog stub for `gbnews`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class GbnewsProvider(StubProvider):
    name = 'gbnews'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('GBNews',)
    source = "catalog"
    description = 'GB News clips, features and live streams'
