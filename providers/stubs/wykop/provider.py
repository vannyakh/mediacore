"""Auto-generated MediaCore catalog stub for `wykop`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class WykopProvider(StubProvider):
    name = 'wykop'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('wykop:dig', 'wykop:\u200bdig:comment', 'wykop:post', 'wykop:\u200bpost:comment')
    source = "catalog"
    description = 'Catalog stub for wykop'
