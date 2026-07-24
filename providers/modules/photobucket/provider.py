"""Auto-generated MediaCore platform module for `photobucket`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class PhotobucketProvider(PlatformModule):
    name = 'photobucket'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('Photobucket',)
    source = "catalog"
    description = 'Platform module for photobucket'
