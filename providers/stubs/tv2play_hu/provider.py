"""Auto-generated MediaCore catalog stub for `tv2play.hu`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class Tv2playHuProvider(StubProvider):
    name = 'tv2play.hu'
    status = 'not_configured'
    host_suffixes = ('tv2play.hu',)
    ie_names = ('tv2play.hu',)
    source = "catalog"
    description = 'Catalog stub for tv2play.hu'
