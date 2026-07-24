"""Auto-generated MediaCore platform module for `fc2`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class Fc2Provider(PlatformModule):
    name = 'fc2'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('fc2', 'fc2:embed', 'fc2:live')
    source = "catalog"
    description = 'Platform module for fc2'
