"""Auto-generated MediaCore catalog stub for `crunchyroll`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class CrunchyrollProvider(StubProvider):
    name = 'crunchyroll'
    status = 'not_configured'
    host_suffixes = ('crunchyroll.com', 'www.crunchyroll.com')
    ie_names = ('Crunchyroll',)
    source = "catalog"
    description = 'Catalog stub for crunchyroll'
