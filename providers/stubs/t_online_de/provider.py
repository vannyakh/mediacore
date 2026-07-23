"""Auto-generated MediaCore catalog stub for `t-online.de`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class TOnlineDeProvider(StubProvider):
    name = 't-online.de'
    status = 'broken'
    host_suffixes = ('t-online.de',)
    ie_names = ('t-online.de',)
    source = "catalog"
    description = 'Catalog stub for t-online.de'
