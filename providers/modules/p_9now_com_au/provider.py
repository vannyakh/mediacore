"""Auto-generated MediaCore platform module for `9now.com.au`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class P9nowComAuProvider(PlatformModule):
    name = '9now.com.au'
    status = 'not_configured'
    host_suffixes = ('9now.com.au', 'www.9now.com.au')
    ie_names = ('9now.com.au',)
    source = "catalog"
    description = 'Platform module for 9now.com.au'
