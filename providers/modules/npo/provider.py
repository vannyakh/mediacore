"""Auto-generated MediaCore platform module for `npo`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class NpoProvider(PlatformModule):
    name = 'npo'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('npo',)
    source = "catalog"
    description = 'npo.nl, ntr.nl, omroepwnl.nl, zapp.nl and npo3.nl'
