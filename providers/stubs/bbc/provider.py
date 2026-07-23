"""Auto-generated MediaCore catalog stub for `bbc`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class BbcProvider(StubProvider):
    name = 'bbc'
    status = 'not_configured'
    host_suffixes = ('bbc.co.uk', 'www.bbc.co.uk', 'bbc.com', 'www.bbc.com')
    ie_names = ('bbc', 'BBC')
    source = "catalog"
    description = 'BBC'
