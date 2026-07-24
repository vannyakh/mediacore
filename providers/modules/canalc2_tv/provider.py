"""Auto-generated MediaCore platform module for `canalc2.tv`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class Canalc2TvProvider(PlatformModule):
    name = 'canalc2.tv'
    status = 'not_configured'
    host_suffixes = ('canalc2.tv', 'www.canalc2.tv', 'archives-canalc2.u-strasbg.fr')
    ie_names = ('canalc2.tv',)
    source = "catalog"
    description = 'Platform module for canalc2.tv'
