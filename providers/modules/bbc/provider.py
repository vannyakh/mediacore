"""Auto-generated MediaCore platform module for `bbc`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class BbcProvider(PlatformModule):
    name = 'bbc'
    status = 'not_configured'
    host_suffixes = ('bbc.co.uk', 'www.bbc.co.uk', 'bbc.com', 'www.bbc.com')
    ie_names = ('bbc', 'BBC')
    source = "catalog"
    description = 'BBC'
