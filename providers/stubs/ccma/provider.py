"""Auto-generated MediaCore catalog stub for `ccma`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class CcmaProvider(StubProvider):
    name = 'ccma'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('CCMA',)
    source = "catalog"
    description = '3Cat, TV3 and Catalunya Ràdio'
