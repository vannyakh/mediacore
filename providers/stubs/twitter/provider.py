"""Auto-generated MediaCore catalog stub for `twitter`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class TwitterProvider(StubProvider):
    name = 'twitter'
    status = 'not_configured'
    host_suffixes = ('twitter.com', 'www.twitter.com', 'x.com', 'www.x.com', 'mobile.twitter.com')
    ie_names = ('twitter', 'Twitter', 'twitter:amplify', 'twitter:broadcast', 'twitter:card', 'twitter:shortener', 'twitter:spaces')
    source = "catalog"
    description = 'Catalog stub for twitter'
