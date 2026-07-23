"""Auto-generated MediaCore catalog stub for `teachertube`.

Upgrade this file to a working provider using official/permitted APIs only.
Regenerate with: uv run python scripts/materialize_catalog_providers.py
"""

from __future__ import annotations

from providers.base_stub import StubProvider


class TeachertubeProvider(StubProvider):
    name = 'teachertube'
    status = 'broken'
    host_suffixes = ()
    ie_names = ('teachertube', 'teachertube:\u200buser:collection')
    source = "catalog"
    description = 'teachertube.com videos'
