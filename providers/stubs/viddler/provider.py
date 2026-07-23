"""Auto-generated MediaCore catalog stub for `viddler`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class ViddlerProvider(StubProvider):
    name = 'viddler'
    status = 'broken'
    host_suffixes = ()
    ie_names = ('Viddler',)
    source = "catalog"
    description = 'Catalog stub for viddler'
