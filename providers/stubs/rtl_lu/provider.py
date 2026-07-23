"""Auto-generated MediaCore catalog stub for `rtl.lu`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class RtlLuProvider(StubProvider):
    name = 'rtl.lu'
    status = 'not_configured'
    host_suffixes = ('rtl.lu',)
    ie_names = ('rtl.lu:article', 'rtl.lu:tele-vod')
    source = "catalog"
    description = 'Catalog stub for rtl.lu'
