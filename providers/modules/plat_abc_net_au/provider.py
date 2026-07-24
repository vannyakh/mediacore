"""Auto-generated MediaCore platform module for `abc.net.au`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class PlatAbcNetAuProvider(PlatformModule):
    name = 'abc.net.au'
    status = 'not_configured'
    host_suffixes = ('abc.net.au', 'www.abc.net.au', 'iview.abc.net.au')
    ie_names = ('abc.net.au', 'abc.net.au:iview', 'abc.net.au:iview:showseries', 'abc.net.au:\u200biview:showseries')
    source = "catalog"
    description = 'Platform module for abc.net.au'
