"""Auto-generated MediaCore catalog stub for `murrtubeuser`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class MurrtubeuserProvider(StubProvider):
    name = 'murrtubeuser'
    status = 'broken'
    host_suffixes = ()
    ie_names = ('MurrtubeUser',)
    source = "catalog"
    description = 'Murrtube user profile'
