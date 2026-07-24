"""Auto-generated MediaCore platform module for `mediaklikk`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class MediaklikkProvider(PlatformModule):
    name = 'mediaklikk'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('MediaKlikk',)
    source = "catalog"
    description = 'Platform module for mediaklikk'
