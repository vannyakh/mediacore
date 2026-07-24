"""Auto-generated MediaCore platform module for `megatvcom`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class MegatvcomProvider(PlatformModule):
    name = 'megatvcom'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('megatvcom', 'megatvcom:embed')
    source = "catalog"
    description = 'megatv.com videos'
