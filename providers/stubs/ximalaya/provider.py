"""Auto-generated MediaCore catalog stub for `ximalaya`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class XimalayaProvider(StubProvider):
    name = 'ximalaya'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('ximalaya', 'ximalaya:album')
    source = "catalog"
    description = '喜马拉雅FM'
