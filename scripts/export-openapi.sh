#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
uv run python -c "from packages.sdk_generator import export_openapi; print(export_openapi())"
