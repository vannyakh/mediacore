"""Auto-generated MediaCore platform module for `svt`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class SvtProvider(PlatformModule):
    name = 'svt'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('svt:page', 'svt:play', 'svt:\u200bplay:series')
    source = "catalog"
    description = 'SVT Play and Öppet arkiv'
