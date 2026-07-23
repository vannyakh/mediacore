"""Auto-generated MediaCore catalog stub for `soundcloud`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class SoundcloudProvider(StubProvider):
    name = 'soundcloud'
    status = 'not_configured'
    host_suffixes = ('soundcloud.com', 'www.soundcloud.com', 'm.soundcloud.com')
    ie_names = ('soundcloud', 'Soundcloud', 'soundcloud:playlist', 'soundcloud:related', 'soundcloud:search', 'soundcloud:set', 'soundcloud:trackstation', 'soundcloud:user', 'soundcloud:\u200buser:permalink')
    source = "catalog"
    description = 'Soundcloud search; "scsearch:" prefix'
