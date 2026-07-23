"""Auto-generated MediaCore catalog stub for `nbcsports`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class NbcsportsProvider(StubProvider):
    name = 'nbcsports'
    status = 'broken'
    host_suffixes = ()
    ie_names = ('NBCSports',)
    source = "catalog"
    description = 'Catalog stub for nbcsports'
