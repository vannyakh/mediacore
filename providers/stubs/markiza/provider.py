"""Auto-generated MediaCore catalog stub for `markiza`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class MarkizaProvider(StubProvider):
    name = 'markiza'
    status = 'broken'
    host_suffixes = ()
    ie_names = ('Markiza',)
    source = "catalog"
    description = 'Catalog stub for markiza'
