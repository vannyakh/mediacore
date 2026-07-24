"""Auto-generated MediaCore platform module for `rtl.nl`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class RtlNlProvider(PlatformModule):
    name = 'rtl.nl'
    status = 'not_configured'
    host_suffixes = ('rtl.nl',)
    ie_names = ('rtl.nl',)
    source = "catalog"
    description = 'rtl.nl and rtlxl.nl'
