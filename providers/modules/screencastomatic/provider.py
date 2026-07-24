"""Auto-generated MediaCore platform module for `screencastomatic`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class ScreencastomaticProvider(PlatformModule):
    name = 'screencastomatic'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('ScreencastOMatic',)
    source = "catalog"
    description = 'Platform module for screencastomatic'
