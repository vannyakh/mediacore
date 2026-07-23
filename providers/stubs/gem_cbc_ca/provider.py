"""Auto-generated MediaCore catalog stub for `gem.cbc.ca`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class GemCbcCaProvider(StubProvider):
    name = 'gem.cbc.ca'
    status = 'not_configured'
    host_suffixes = ('gem.cbc.ca',)
    ie_names = ('gem.cbc.ca', 'gem.cbc.ca:live', 'gem.cbc.ca:olympics', 'gem.cbc.ca:playlist')
    source = "catalog"
    description = 'Catalog stub for gem.cbc.ca'
