"""Auto-generated MediaCore platform module for `yandexmusic`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class YandexmusicProvider(PlatformModule):
    name = 'yandexmusic'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('yandexmusic:album', 'yandexmusic:\u200bartist:albums', 'yandexmusic:\u200bartist:tracks', 'yandexmusic:playlist', 'yandexmusic:track')
    source = "catalog"
    description = 'Яндекс.Музыка - Альбом'
