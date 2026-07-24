"""Auto-generated MediaCore platform module for `sbs.co.kr`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class SbsCoKrProvider(PlatformModule):
    name = 'sbs.co.kr'
    status = 'not_configured'
    host_suffixes = ('sbs.co.kr',)
    ie_names = ('sbs.co.kr', 'sbs.co.kr:allvod_program', 'sbs.co.kr:programs_vod')
    source = "catalog"
    description = 'Platform module for sbs.co.kr'
