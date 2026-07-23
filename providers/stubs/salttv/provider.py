"""Auto-generated MediaCore catalog stub for `salttv`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class SalttvProvider(StubProvider):
    name = 'salttv'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('SaltTV',)
    source = "catalog"
    description = 'Catalog stub for salttv'
