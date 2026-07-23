"""Auto-generated MediaCore catalog stub for `linkedin`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class LinkedinProvider(StubProvider):
    name = 'linkedin'
    status = 'not_configured'
    host_suffixes = ('linkedin.com', 'www.linkedin.com')
    ie_names = ('LinkedIn', 'linkedin', 'linkedin:events', 'linkedin:learning', 'linkedin:\u200blearning:course')
    source = "catalog"
    description = 'Catalog stub for linkedin'
