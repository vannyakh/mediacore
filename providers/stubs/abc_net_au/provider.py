"""Auto-generated MediaCore catalog stub for `abc.net.au`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class AbcNetAuProvider(StubProvider):
    name = 'abc.net.au'
    status = 'not_configured'
    host_suffixes = ('abc.net.au',)
    ie_names = ('abc.net.au', 'abc.net.au:iview', 'abc.net.au:\u200biview:showseries')
    source = "catalog"
    description = 'Catalog stub for abc.net.au'
