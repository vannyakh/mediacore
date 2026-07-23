"""Auto-generated MediaCore catalog stub for `tunein`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class TuneinProvider(StubProvider):
    name = 'tunein'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('tunein:embed', 'tunein:podcast', 'tunein:\u200bpodcast:program', 'tunein:station')
    source = "catalog"
    description = 'Catalog stub for tunein'
