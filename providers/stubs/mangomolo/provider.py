"""Auto-generated MediaCore catalog stub for `mangomolo`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class MangomoloProvider(StubProvider):
    name = 'mangomolo'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('mangomolo:live', 'mangomolo:video')
    source = "catalog"
    description = 'Catalog stub for mangomolo'
