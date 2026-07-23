"""Auto-generated MediaCore catalog stub for `loom`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class LoomProvider(StubProvider):
    name = 'loom'
    status = 'broken'
    host_suffixes = ('loom.com', 'www.loom.com')
    ie_names = ('loom', 'Loom', 'loom:folder')
    source = "catalog"
    description = 'Catalog stub for loom'
