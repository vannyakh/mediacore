"""Auto-generated MediaCore catalog stub for `yandexmusic`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class YandexmusicProvider(StubProvider):
    name = 'yandexmusic'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('yandexmusic:album', 'yandexmusic:\u200bartist:albums', 'yandexmusic:\u200bartist:tracks', 'yandexmusic:playlist', 'yandexmusic:track')
    source = "catalog"
    description = 'Яндекс.Музыка - Альбом'
