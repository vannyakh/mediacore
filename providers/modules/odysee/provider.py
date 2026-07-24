"""Auto-generated MediaCore platform module for `odysee`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class OdyseeProvider(PlatformModule):
    name = 'odysee'
    status = 'not_configured'
    host_suffixes = ('odysee.com', 'www.odysee.com')
    ie_names = ('lbry', 'Odysee', 'lbry:channel', 'lbry:playlist')
    source = "catalog"
    description = 'odysee.com'
