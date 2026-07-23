"""Auto-generated MediaCore catalog stub for `qqmusic`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class QqmusicProvider(StubProvider):
    name = 'qqmusic'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('qqmusic', 'qqmusic:album', 'qqmusic:mv', 'qqmusic:playlist', 'qqmusic:singer', 'qqmusic:toplist')
    source = "catalog"
    description = 'QQ音乐'
