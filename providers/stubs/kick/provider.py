"""Auto-generated MediaCore catalog stub for `kick`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class KickProvider(StubProvider):
    name = 'kick'
    status = 'not_configured'
    host_suffixes = ('kick.com', 'www.kick.com')
    ie_names = ('kick:clips', 'Kick', 'kick:live', 'kick:vod')
    source = "catalog"
    description = 'Catalog stub for kick'
