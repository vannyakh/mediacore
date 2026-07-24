"""Auto-generated MediaCore platform module for `nova`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class NovaProvider(PlatformModule):
    name = 'nova'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('Nova',)
    source = "catalog"
    description = 'TN.cz, Prásk.tv, Nova.cz, Novaplus.cz, FANDA.tv, Krásná.cz and Doma.cz'
