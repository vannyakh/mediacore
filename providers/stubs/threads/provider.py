"""Auto-generated MediaCore catalog stub for `threads`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class ThreadsProvider(StubProvider):
    name = 'threads'
    status = 'not_configured'
    host_suffixes = ('threads.net', 'www.threads.net')
    ie_names = ('Threads',)
    source = "catalog"
    description = 'Catalog stub for threads'
