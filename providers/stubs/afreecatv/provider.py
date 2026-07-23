"""Auto-generated MediaCore catalog stub for `afreecatv`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class AfreecatvProvider(StubProvider):
    name = 'afreecatv'
    status = 'not_configured'
    host_suffixes = ('afreecatv.com', 'www.afreecatv.com', 'vod.afreecatv.com')
    ie_names = ('afreecatv',)
    source = "catalog"
    description = 'Catalog stub for afreecatv'
