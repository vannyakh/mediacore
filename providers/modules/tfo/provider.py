"""Auto-generated MediaCore platform module for `tfo`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class TfoProvider(PlatformModule):
    name = 'tfo'
    status = 'broken'
    host_suffixes = ()
    ie_names = ('TFO',)
    source = "catalog"
    description = 'Platform module for tfo'
