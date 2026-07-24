"""Auto-generated MediaCore platform module for `tunein`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class TuneinProvider(PlatformModule):
    name = 'tunein'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('tunein:embed', 'tunein:podcast', 'tunein:\u200bpodcast:program', 'tunein:station')
    source = "catalog"
    description = 'Platform module for tunein'
