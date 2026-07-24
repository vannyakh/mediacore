"""Auto-generated MediaCore platform module for `funimation`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class FunimationProvider(PlatformModule):
    name = 'funimation'
    status = 'not_configured'
    host_suffixes = ('funimation.com', 'www.funimation.com')
    ie_names = ('Funimation',)
    source = "catalog"
    description = 'Platform module for funimation'
