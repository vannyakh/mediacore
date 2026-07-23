"""Auto-generated MediaCore catalog stub for `la7.it`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class La7ItProvider(StubProvider):
    name = 'la7.it'
    status = 'not_configured'
    host_suffixes = ('la7.it',)
    ie_names = ('la7.it', 'la7.it:\u200bpod:episode', 'la7.it:podcast')
    source = "catalog"
    description = 'Catalog stub for la7.it'
