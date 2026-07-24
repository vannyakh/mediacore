"""Auto-generated MediaCore platform module for `youpornchannel`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class YoupornchannelProvider(PlatformModule):
    name = 'youpornchannel'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('YouPornChannel',)
    source = "catalog"
    description = 'YouPorn channel, with sorting and pagination'
