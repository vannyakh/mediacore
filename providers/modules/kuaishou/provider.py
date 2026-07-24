"""Auto-generated MediaCore platform module for `kuaishou`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class KuaishouProvider(PlatformModule):
    name = 'kuaishou'
    status = 'not_configured'
    host_suffixes = ('kuaishou.com', 'www.kuaishou.com', 'v.kuaishou.com')
    ie_names = ('Kuaishou',)
    source = "catalog"
    description = 'Platform module for kuaishou'
