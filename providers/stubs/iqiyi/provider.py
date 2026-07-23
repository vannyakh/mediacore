"""Auto-generated MediaCore catalog stub for `iqiyi`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class IqiyiProvider(StubProvider):
    name = 'iqiyi'
    status = 'not_configured'
    host_suffixes = ('iqiyi.com', 'www.iqiyi.com')
    ie_names = ('iqiyi',)
    source = "catalog"
    description = '爱奇艺'
