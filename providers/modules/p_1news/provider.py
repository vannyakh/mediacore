"""Auto-generated MediaCore platform module for `1news`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class P1newsProvider(PlatformModule):
    name = '1news'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('1News',)
    source = "catalog"
    description = '1news.co.nz article videos'
