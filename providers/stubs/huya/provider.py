"""Auto-generated MediaCore catalog stub for `huya`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class HuyaProvider(StubProvider):
    name = 'huya'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('huya:live', 'huya:video')
    source = "catalog"
    description = '虎牙直播'
