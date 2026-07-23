"""Export OpenAPI schema for SDK generators."""

from __future__ import annotations

import json
from pathlib import Path


def export_openapi(dest: str | Path = "docs/openapi.json") -> Path:
    from apps.api.main import create_app

    app = create_app()
    path = Path(dest)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(app.openapi(), indent=2), encoding="utf-8")
    return path
