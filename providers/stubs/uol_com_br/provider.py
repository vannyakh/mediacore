"""Auto-generated MediaCore catalog stub for `uol.com.br`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class UolComBrProvider(StubProvider):
    name = 'uol.com.br'
    status = 'not_configured'
    host_suffixes = ('uol.com.br',)
    ie_names = ('uol.com.br',)
    source = "catalog"
    description = 'Catalog stub for uol.com.br'
