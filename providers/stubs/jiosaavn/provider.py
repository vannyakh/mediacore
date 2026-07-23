"""Auto-generated MediaCore catalog stub for `jiosaavn`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class JiosaavnProvider(StubProvider):
    name = 'jiosaavn'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('jiosaavn:album', 'jiosaavn:artist', 'jiosaavn:playlist', 'jiosaavn:show', 'jiosaavn:\u200bshow:playlist', 'jiosaavn:song')
    source = "catalog"
    description = 'Catalog stub for jiosaavn'
