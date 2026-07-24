"""Auto-generated MediaCore platform module for `rtvslo.si`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class RtvsloSiProvider(PlatformModule):
    name = 'rtvslo.si'
    status = 'not_configured'
    host_suffixes = ('rtvslo.si',)
    ie_names = ('rtvslo.si', 'rtvslo.si:show')
    source = "catalog"
    description = 'Platform module for rtvslo.si'
