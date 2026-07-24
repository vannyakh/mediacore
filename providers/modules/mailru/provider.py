"""Auto-generated MediaCore platform module for `mailru`.

Direct media URLs on this module's hosts support metadata + download.
Page/watch URLs need an official/permitted API upgrade.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_module import PlatformModule


class MailruProvider(PlatformModule):
    name = 'mailru'
    status = 'not_configured'
    host_suffixes = ()
    ie_names = ('mailru', 'mailru:music', 'mailru:\u200bmusic:search')
    source = "catalog"
    description = 'Видео@Mail.Ru'
