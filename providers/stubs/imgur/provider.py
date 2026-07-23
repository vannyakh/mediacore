"""Auto-generated MediaCore catalog stub for `imgur`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class ImgurProvider(StubProvider):
    name = 'imgur'
    status = 'not_configured'
    host_suffixes = ('imgur.com', 'i.imgur.com', 'www.imgur.com')
    ie_names = ('Imgur', 'imgur:album', 'imgur:gallery')
    source = "catalog"
    description = 'Catalog stub for imgur'
