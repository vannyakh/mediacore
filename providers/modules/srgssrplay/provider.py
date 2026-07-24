"""Auto-generated MediaCore platform module for `srgssrplay`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class SrgssrplayProvider(PlatformModule):
    name = 'srgssrplay'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('SRGSSRPlay',)
    source = "catalog"
    description = 'srf.ch, rts.ch, rsi.ch, rtr.ch and swissinfo.ch play sites'
