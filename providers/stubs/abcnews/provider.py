"""Auto-generated MediaCore catalog stub for `abcnews`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class AbcnewsProvider(StubProvider):
    name = 'abcnews'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('abcnews', 'abcnews:video')
    source = "catalog"
    description = 'Catalog stub for abcnews'
