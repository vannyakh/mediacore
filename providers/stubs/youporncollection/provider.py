"""Auto-generated MediaCore catalog stub for `youporncollection`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class YouporncollectionProvider(StubProvider):
    name = 'youporncollection'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('YouPornCollection',)
    source = "catalog"
    description = 'YouPorn collection (user playlist), with sorting and pagination'
