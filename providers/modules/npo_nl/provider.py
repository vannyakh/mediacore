"""Auto-generated MediaCore platform module for `npo.nl`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class NpoNlProvider(PlatformModule):
    name = 'npo.nl'
    status = 'not_configured'
    host_suffixes = ('npo.nl',)
    ie_names = ('npo.nl:live', 'npo.nl:radio', 'npo.nl:\u200bradio:fragment')
    source = "catalog"
    description = 'Platform module for npo.nl'
