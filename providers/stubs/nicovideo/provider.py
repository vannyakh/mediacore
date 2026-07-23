"""Auto-generated MediaCore catalog stub for `nicovideo`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class NicovideoProvider(StubProvider):
    name = 'nicovideo'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('nicovideo:search', 'nicovideo:\u200bsearch:date', 'nicovideo:search_url')
    source = "catalog"
    description = 'Nico video search; "nicosearch:" prefix'
