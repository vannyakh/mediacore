"""Auto-generated MediaCore platform module for `orf`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class OrfProvider(PlatformModule):
    name = 'orf'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('orf:\u200bfm4:story', 'orf:iptv', 'orf:on', 'orf:podcast', 'orf:radio')
    source = "catalog"
    description = 'fm4.orf.at stories'
