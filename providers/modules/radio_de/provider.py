"""Auto-generated MediaCore platform module for `radio.de`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class RadioDeProvider(PlatformModule):
    name = 'radio.de'
    status = 'broken'
    host_suffixes = ('radio.de',)
    ie_names = ('radio.de',)
    source = "catalog"
    description = 'Platform module for radio.de'
