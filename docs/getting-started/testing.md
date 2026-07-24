---
title: Testing
---

<script setup>
const links = [
  { title: "Plugins", href: "/plugins/", hint: "Contract tests", icon: "https://cdn.simpleicons.org/npm/CB3837" },
  { title: "Platforms", href: "/platforms/", hint: "Provider contracts", icon: "https://cdn.simpleicons.org/youtube/FF0000" },
  { title: "Get started", href: "/getting-started/", hint: "Local setup", icon: "https://cdn.simpleicons.org/python/3776AB" },
]
const gates = [
  { value: "PR", label: "unit · api · contracts" },
  { value: "Nightly", label: "stress · chaos" },
  { value: "≥40%", label: "Coverage floor" },
  { value: "TestKit", label: "Shared fakes" },
]
</script>

<DocHero
  eyebrow="Quality"
  title="Testing"
  lead="Layered suites for the download CLI/API, providers, and remaining plugins."
/>

<DocStats :items="gates" />

## Run locally

```bash
uv sync --extra dev

# Download-tool focused
uv run pytest tests/unit/cli tests/providers -q --benchmark-disable

# PR-critical suite
uv run pytest -m "not load and not stress and not chaos and not benchmark" --benchmark-disable
```

## Markers

| Marker | PR CI | Nightly |
|--------|-------|---------|
| unit, integration, api, provider, plugin, storage | yes | yes |
| e2e, performance, security, regression | yes | yes |
| stress, chaos | no | yes |

## Continue

<DocLinks :items="links" />
