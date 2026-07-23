#!/usr/bin/env bash
set -euo pipefail
URL="${1:-https://example.com/video.mp4}"
curl -s -H "X-API-Key: ${MEDIACORE_API_KEY:-dev-api-key-change-me}" \
  -H "Content-Type: application/json" \
  -d "{\"url\":\"${URL}\"}" \
  "${MEDIACORE_BASE:-http://localhost:8000}/v1/analyze" | python -m json.tool
