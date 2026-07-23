"""Auto-generated MediaCore catalog stub for `instagram`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class InstagramProvider(StubProvider):
    name = 'instagram'
    status = 'broken'
    host_suffixes = ('instagram.com', 'www.instagram.com')
    ie_names = ('Instagram', 'instagram:story', 'instagram:tag', 'instagram:user')
    source = "catalog"
    description = 'Instagram hashtag search URLs'
