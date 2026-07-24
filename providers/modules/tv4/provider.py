"""Auto-generated MediaCore platform module for `tv4`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class Tv4Provider(PlatformModule):
    name = 'tv4'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('TV4',)
    source = "catalog"
    description = 'tv4.se and tv4play.se'
