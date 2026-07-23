"""Auto-generated MediaCore catalog stub for `jwplatform`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class JwplatformProvider(StubProvider):
    name = 'jwplatform'
    status = 'not_configured'
    host_suffixes = ('jwplatform.com', 'cdn.jwplayer.com')
    ie_names = ('JWPlatform',)
    source = "catalog"
    description = 'Catalog stub for jwplatform'
