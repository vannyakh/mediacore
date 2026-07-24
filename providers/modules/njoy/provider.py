"""Auto-generated MediaCore platform module for `njoy`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class NjoyProvider(PlatformModule):
    name = 'njoy'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('njoy', 'njoy:embed')
    source = "catalog"
    description = 'N-JOY'
