"""Auto-generated MediaCore catalog stub for `snapchat`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class SnapchatProvider(StubProvider):
    name = 'snapchat'
    status = 'not_configured'
    host_suffixes = ('snapchat.com', 'www.snapchat.com', 'story.snapchat.com')
    ie_names = ('Snapchat',)
    source = "catalog"
    description = 'Catalog stub for snapchat'
