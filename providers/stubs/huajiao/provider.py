"""Auto-generated MediaCore catalog stub for `huajiao`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class HuajiaoProvider(StubProvider):
    name = 'huajiao'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('Huajiao',)
    source = "catalog"
    description = '花椒直播'
