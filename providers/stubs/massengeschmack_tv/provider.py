"""Auto-generated MediaCore catalog stub for `massengeschmack.tv`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class MassengeschmackTvProvider(StubProvider):
    name = 'massengeschmack.tv'
    status = 'not_configured'
    host_suffixes = ('massengeschmack.tv',)
    ie_names = ('massengeschmack.tv',)
    source = "catalog"
    description = 'Catalog stub for massengeschmack.tv'
