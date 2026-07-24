"""Auto-generated MediaCore platform module for `gem.cbc.ca`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class GemCbcCaProvider(PlatformModule):
    name = 'gem.cbc.ca'
    status = 'not_configured'
    host_suffixes = ('gem.cbc.ca',)
    ie_names = ('gem.cbc.ca', 'gem.cbc.ca:live', 'gem.cbc.ca:olympics', 'gem.cbc.ca:playlist')
    source = "catalog"
    description = 'Platform module for gem.cbc.ca'
