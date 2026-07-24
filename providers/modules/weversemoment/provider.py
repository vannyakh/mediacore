"""Auto-generated MediaCore platform module for `weversemoment`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class WeversemomentProvider(PlatformModule):
    name = 'weversemoment'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('WeverseMoment',)
    source = "catalog"
    description = 'Platform module for weversemoment'
