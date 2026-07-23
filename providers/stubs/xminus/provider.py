"""Auto-generated MediaCore catalog stub for `xminus`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class XminusProvider(StubProvider):
    name = 'xminus'
    status = 'broken'
    host_suffixes = ()
    ie_names = ('XMinus',)
    source = "catalog"
    description = 'Catalog stub for xminus'
