"""Auto-generated MediaCore catalog stub for `parler`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class ParlerProvider(StubProvider):
    name = 'parler'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('Parler',)
    source = "catalog"
    description = 'Posts on parler.com'
