"""Auto-generated MediaCore catalog stub for `douyutv`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class DouyutvProvider(StubProvider):
    name = 'douyutv'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('DouyuTV',)
    source = "catalog"
    description = '斗鱼直播'
