"""Auto-generated MediaCore catalog stub for `sbs.co.kr`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class SbsCoKrProvider(StubProvider):
    name = 'sbs.co.kr'
    status = 'not_configured'
    host_suffixes = ('sbs.co.kr',)
    ie_names = ('sbs.co.kr', 'sbs.co.kr:allvod_program', 'sbs.co.kr:programs_vod')
    source = "catalog"
    description = 'Catalog stub for sbs.co.kr'
