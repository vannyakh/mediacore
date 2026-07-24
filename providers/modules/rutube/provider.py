"""Auto-generated MediaCore platform module for `rutube`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class RutubeProvider(PlatformModule):
    name = 'rutube'
    status = 'not_configured'
    host_suffixes = ('rutube.ru', 'www.rutube.ru')
    ie_names = ('rutube', 'Rutube', 'rutube:channel', 'rutube:embed', 'rutube:movie', 'rutube:person', 'rutube:playlist', 'rutube:tags')
    source = "catalog"
    description = 'Rutube videos'
