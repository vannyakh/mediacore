"""Auto-generated MediaCore platform module for `peer.tv`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class PeerTvProvider(PlatformModule):
    name = 'peer.tv'
    status = 'not_configured'
    host_suffixes = ('peer.tv',)
    ie_names = ('peer.tv',)
    source = "catalog"
    description = 'Platform module for peer.tv'
