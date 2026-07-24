"""Auto-generated MediaCore platform module for `maariv.co.il`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class MaarivCoIlProvider(PlatformModule):
    name = 'maariv.co.il'
    status = 'not_configured'
    host_suffixes = ('maariv.co.il',)
    ie_names = ('maariv.co.il',)
    source = "catalog"
    description = 'Platform module for maariv.co.il'
