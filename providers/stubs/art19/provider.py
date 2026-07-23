"""Auto-generated MediaCore catalog stub for `art19`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class Art19Provider(StubProvider):
    name = 'art19'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('Art19',)
    source = "catalog"
    description = 'Catalog stub for art19'
