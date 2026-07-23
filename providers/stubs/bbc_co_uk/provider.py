"""Auto-generated MediaCore catalog stub for `bbc.co.uk`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class BbcCoUkProvider(StubProvider):
    name = 'bbc.co.uk'
    status = 'not_configured'
    host_suffixes = ('bbc.co.uk',)
    ie_names = ('bbc.co.uk', 'bbc.co.uk:article', 'bbc.co.uk:\u200biplayer:episodes', 'bbc.co.uk:\u200biplayer:group', 'bbc.co.uk:playlist')
    source = "catalog"
    description = 'BBC iPlayer'
