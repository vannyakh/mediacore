"""Auto-generated MediaCore platform module for `mixlr`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class MixlrProvider(PlatformModule):
    name = 'mixlr'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('Mixlr',)
    source = "catalog"
    description = 'Platform module for mixlr'
