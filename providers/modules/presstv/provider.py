"""Auto-generated MediaCore platform module for `presstv`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class PresstvProvider(PlatformModule):
    name = 'presstv'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('PressTV',)
    source = "catalog"
    description = 'Platform module for presstv'
