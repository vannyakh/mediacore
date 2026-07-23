"""Auto-generated MediaCore catalog stub for `mailru`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class MailruProvider(StubProvider):
    name = 'mailru'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('mailru', 'mailru:music', 'mailru:\u200bmusic:search')
    source = "catalog"
    description = 'Видео@Mail.Ru'
