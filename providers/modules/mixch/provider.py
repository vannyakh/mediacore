"""Auto-generated MediaCore platform module for `mixch`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class MixchProvider(PlatformModule):
    name = 'mixch'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('mixch', 'mixch:archive', 'mixch:movie')
    source = "catalog"
    description = 'Platform module for mixch'
