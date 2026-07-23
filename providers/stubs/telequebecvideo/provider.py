"""Auto-generated MediaCore catalog stub for `telequebecvideo`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class TelequebecvideoProvider(StubProvider):
    name = 'telequebecvideo'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('TeleQuebecVideo',)
    source = "catalog"
    description = 'Catalog stub for telequebecvideo'
