"""Auto-generated MediaCore platform module for `uol.com.br`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class UolComBrProvider(PlatformModule):
    name = 'uol.com.br'
    status = 'not_configured'
    host_suffixes = ('uol.com.br',)
    ie_names = ('uol.com.br',)
    source = "catalog"
    description = 'Platform module for uol.com.br'
