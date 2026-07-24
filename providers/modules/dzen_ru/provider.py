"""Auto-generated MediaCore platform module for `dzen.ru`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class DzenRuProvider(PlatformModule):
    name = 'dzen.ru'
    status = 'not_configured'
    host_suffixes = ('dzen.ru', 'www.dzen.ru', 'zen.yandex.ru')
    ie_names = ('dzen.ru', 'Dzen', 'ZenYandex', 'dzen.ru:channel')
    source = "catalog"
    description = 'Дзен (dzen) formerly Яндекс.Дзен (Yandex Zen)'
