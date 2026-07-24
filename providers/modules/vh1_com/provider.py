"""Auto-generated MediaCore platform module for `vh1.com`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class Vh1ComProvider(PlatformModule):
    name = 'vh1.com'
    status = 'not_configured'
    host_suffixes = ('vh1.com',)
    ie_names = ('vh1.com',)
    source = "catalog"
    description = 'Platform module for vh1.com'
