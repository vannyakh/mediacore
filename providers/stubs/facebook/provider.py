"""Auto-generated MediaCore catalog stub for `facebook`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class FacebookProvider(StubProvider):
    name = 'facebook'
    status = 'not_configured'
    host_suffixes = ('facebook.com', 'www.facebook.com', 'fb.watch', 'm.facebook.com', 'fb.com')
    ie_names = ('facebook', 'Facebook', 'facebook:ads', 'facebook:reel')
    source = "catalog"
    description = 'Catalog stub for facebook'
