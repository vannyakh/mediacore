"""Auto-generated MediaCore catalog stub for `ttinglive`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class TtingliveProvider(StubProvider):
    name = 'ttinglive'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('ttinglive',)
    source = "catalog"
    description = '띵라이브 (formerly FlexTV)'
