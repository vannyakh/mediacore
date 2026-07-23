"""Auto-generated MediaCore catalog stub for `peer.tv`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class PeerTvProvider(StubProvider):
    name = 'peer.tv'
    status = 'not_configured'
    host_suffixes = ('peer.tv',)
    ie_names = ('peer.tv',)
    source = "catalog"
    description = 'Catalog stub for peer.tv'
