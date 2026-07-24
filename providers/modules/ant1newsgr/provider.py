"""Auto-generated MediaCore platform module for `ant1newsgr`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class Ant1newsgrProvider(PlatformModule):
    name = 'ant1newsgr'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('ant1newsgr:article', 'ant1newsgr:embed')
    source = "catalog"
    description = 'ant1news.gr articles'
