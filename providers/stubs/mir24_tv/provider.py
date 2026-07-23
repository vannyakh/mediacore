"""Auto-generated MediaCore catalog stub for `mir24.tv`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class Mir24TvProvider(StubProvider):
    name = 'mir24.tv'
    status = 'not_configured'
    host_suffixes = ('mir24.tv',)
    ie_names = ('mir24.tv',)
    source = "catalog"
    description = 'Catalog stub for mir24.tv'
