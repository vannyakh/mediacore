"""Auto-generated MediaCore catalog stub for `faz.net`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class FazNetProvider(StubProvider):
    name = 'faz.net'
    status = 'not_configured'
    host_suffixes = ('faz.net',)
    ie_names = ('faz.net',)
    source = "catalog"
    description = 'Catalog stub for faz.net'
