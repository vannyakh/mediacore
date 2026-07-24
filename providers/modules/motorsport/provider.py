"""Auto-generated MediaCore platform module for `motorsport`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class MotorsportProvider(PlatformModule):
    name = 'motorsport'
    status = 'broken'
    host_suffixes = ()
    ie_names = ('Motorsport',)
    source = "catalog"
    description = 'motorsport.com'
