"""Auto-generated MediaCore platform module for `bbc.co.uk`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class BbcCoUkProvider(PlatformModule):
    name = 'bbc.co.uk'
    status = 'not_configured'
    host_suffixes = ('bbc.co.uk',)
    ie_names = ('bbc.co.uk', 'bbc.co.uk:article', 'bbc.co.uk:\u200biplayer:episodes', 'bbc.co.uk:\u200biplayer:group', 'bbc.co.uk:playlist')
    source = "catalog"
    description = 'BBC iPlayer'
