#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
export SYNC_DOWNLOAD="${SYNC_DOWNLOAD:-true}"
export USE_SQLITE="${USE_SQLITE:-true}"
uv run uvicorn apps.api.main:app --reload --host 0.0.0.0 --port 8000
