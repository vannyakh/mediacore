"""Auto-generated MediaCore catalog stub for `safari`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class SafariProvider(StubProvider):
    name = 'safari'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('safari', 'safari:api', 'safari:course')
    source = "catalog"
    description = 'safaribooksonline.com online video'
