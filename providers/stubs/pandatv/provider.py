"""Auto-generated MediaCore catalog stub for `pandatv`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class PandatvProvider(StubProvider):
    name = 'pandatv'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('PandaTv',)
    source = "catalog"
    description = 'pandalive.co.kr (팬더티비)'
