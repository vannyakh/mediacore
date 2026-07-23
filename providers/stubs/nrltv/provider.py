"""Auto-generated MediaCore catalog stub for `nrltv`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class NrltvProvider(StubProvider):
    name = 'nrltv'
    status = 'broken'
    host_suffixes = ()
    ie_names = ('NRLTV',)
    source = "catalog"
    description = 'Catalog stub for nrltv'
