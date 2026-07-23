"""Auto-generated MediaCore catalog stub for `mojevideo`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class MojevideoProvider(StubProvider):
    name = 'mojevideo'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('Mojevideo',)
    source = "catalog"
    description = 'mojevideo.sk'
