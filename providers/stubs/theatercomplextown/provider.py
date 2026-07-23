"""Auto-generated MediaCore catalog stub for `theatercomplextown`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class TheatercomplextownProvider(StubProvider):
    name = 'theatercomplextown'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('theatercomplextown:ppv', 'theatercomplextown:vod')
    source = "catalog"
    description = 'Catalog stub for theatercomplextown'
