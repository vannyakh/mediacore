"""Auto-generated MediaCore catalog stub for `dzen.ru`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class DzenRuProvider(StubProvider):
    name = 'dzen.ru'
    status = 'not_configured'
    host_suffixes = ('dzen.ru',)
    ie_names = ('dzen.ru', 'dzen.ru:channel')
    source = "catalog"
    description = 'Дзен (dzen) formerly Яндекс.Дзен (Yandex Zen)'
