"""Auto-generated MediaCore platform module for `ocw.mit.edu`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class OcwMitEduProvider(PlatformModule):
    name = 'ocw.mit.edu'
    status = 'not_configured'
    host_suffixes = ('ocw.mit.edu',)
    ie_names = ('ocw.mit.edu',)
    source = "catalog"
    description = 'Platform module for ocw.mit.edu'
