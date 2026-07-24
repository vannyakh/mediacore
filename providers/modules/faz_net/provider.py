"""Auto-generated MediaCore platform module for `faz.net`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class FazNetProvider(PlatformModule):
    name = 'faz.net'
    status = 'not_configured'
    host_suffixes = ('faz.net', 'www.faz.net')
    ie_names = ('faz.net', 'FAZ')
    source = "catalog"
    description = 'Platform module for faz.net'
