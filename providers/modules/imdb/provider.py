"""Auto-generated MediaCore platform module for `imdb`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class ImdbProvider(PlatformModule):
    name = 'imdb'
    status = 'not_configured'
    host_suffixes = ('imdb.com', 'www.imdb.com', 'm.imdb.com')
    ie_names = ('imdb', 'imdb:list')
    source = "catalog"
    description = 'Internet Movie Database trailers'
