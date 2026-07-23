"""Auto-generated MediaCore catalog stub for `arte.sky.it`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class ArteSkyItProvider(StubProvider):
    name = 'arte.sky.it'
    status = 'not_configured'
    host_suffixes = ('arte.sky.it',)
    ie_names = ('arte.sky.it',)
    source = "catalog"
    description = 'Catalog stub for arte.sky.it'
