"""Auto-generated MediaCore catalog stub for `sangiin`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class SangiinProvider(StubProvider):
    name = 'sangiin'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('Sangiin',)
    source = "catalog"
    description = '参議院インターネット審議中継 (archive)'
