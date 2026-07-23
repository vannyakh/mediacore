"""Auto-generated MediaCore catalog stub for `rutube`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class RutubeProvider(StubProvider):
    name = 'rutube'
    status = 'not_configured'
    host_suffixes = ('rutube.ru', 'www.rutube.ru')
    ie_names = ('rutube', 'Rutube', 'rutube:channel', 'rutube:embed', 'rutube:movie', 'rutube:person', 'rutube:playlist', 'rutube:tags')
    source = "catalog"
    description = 'Rutube videos'
