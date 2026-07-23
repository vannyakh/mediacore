"""Auto-generated MediaCore catalog stub for `tv8.it`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class Tv8ItProvider(StubProvider):
    name = 'tv8.it'
    status = 'not_configured'
    host_suffixes = ('tv8.it',)
    ie_names = ('tv8.it', 'tv8.it:live', 'tv8.it:playlist')
    source = "catalog"
    description = 'TV8 Live'
