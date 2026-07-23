"""Auto-generated MediaCore catalog stub for `jeuxvideo`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class JeuxvideoProvider(StubProvider):
    name = 'jeuxvideo'
    status = 'broken'
    host_suffixes = ()
    ie_names = ('JeuxVideo',)
    source = "catalog"
    description = 'Catalog stub for jeuxvideo'
