"""Auto-generated MediaCore catalog stub for `funimation`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class FunimationProvider(StubProvider):
    name = 'funimation'
    status = 'not_configured'
    host_suffixes = ('funimation.com', 'www.funimation.com')
    ie_names = ('Funimation',)
    source = "catalog"
    description = 'Catalog stub for funimation'
