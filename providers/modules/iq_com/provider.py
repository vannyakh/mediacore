"""Auto-generated MediaCore platform module for `iq.com`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class IqComProvider(PlatformModule):
    name = 'iq.com'
    status = 'not_configured'
    host_suffixes = ('iq.com', 'www.iq.com')
    ie_names = ('iq.com', 'iq.com:album')
    source = "catalog"
    description = 'International version of iQiyi'
