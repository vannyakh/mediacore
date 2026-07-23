"""Auto-generated MediaCore catalog stub for `soop`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class SoopProvider(StubProvider):
    name = 'soop'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('soop', 'soop:catchstory', 'soop:live', 'soop:user')
    source = "catalog"
    description = 'sooplive.com'
