"""Auto-generated MediaCore platform module for `rtve.es`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class RtveEsProvider(PlatformModule):
    name = 'rtve.es'
    status = 'not_configured'
    host_suffixes = ('rtve.es',)
    ie_names = ('rtve.es:alacarta', 'rtve.es:audio', 'rtve.es:live', 'rtve.es:program', 'rtve.es:television')
    source = "catalog"
    description = 'RTVE a la carta and Play'
