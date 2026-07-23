"""Auto-generated MediaCore catalog stub for `euscreen`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class EuscreenProvider(StubProvider):
    name = 'euscreen'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('EUScreen',)
    source = "catalog"
    description = 'Catalog stub for euscreen'
