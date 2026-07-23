"""Auto-generated MediaCore catalog stub for `media.ccc.de`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class MediaCccDeProvider(StubProvider):
    name = 'media.ccc.de'
    status = 'not_configured'
    host_suffixes = ('media.ccc.de',)
    ie_names = ('media.ccc.de', 'media.ccc.de:lists')
    source = "catalog"
    description = 'Catalog stub for media.ccc.de'
