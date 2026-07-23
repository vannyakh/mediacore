"""Auto-generated MediaCore catalog stub for `kuwo`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class KuwoProvider(StubProvider):
    name = 'kuwo'
    status = 'broken'
    host_suffixes = ()
    ie_names = ('kuwo:album', 'kuwo:category', 'kuwo:chart', 'kuwo:mv', 'kuwo:singer', 'kuwo:song')
    source = "catalog"
    description = '酷我音乐 - 专辑'
