"""Auto-generated MediaCore catalog stub for `art19show`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class Art19showProvider(StubProvider):
    name = 'art19show'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('Art19Show',)
    source = "catalog"
    description = 'Catalog stub for art19show'
