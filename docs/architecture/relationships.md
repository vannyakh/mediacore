---
title: Relationships
---

# Package relationships

Interactive dependency map of MediaCore packages, apps, providers, plugins, and SDKs — similar to monorepo “relationships” views.

Drag nodes, scroll to zoom, and use the sidebar filters.

<DependencyGraph />

## How to read the graph

| Color / style | Meaning |
|---------------|---------|
| Blue nodes | Core packages (`packages/*`) |
| Purple nodes | Apps (`apps/api`, worker, CLI) |
| Green nodes | Providers / extractors |
| Amber nodes | Plugins |
| Pink nodes | SDKs |
| Gray nodes | External infrastructure |
| Solid pink edge | Production dependency |
| Dashed purple edge | Optional (cloud, Redis, FFmpeg binary) |

## Related

- [Architecture overview](./overview)
- [Register an extractor](/platforms/register)
- [Register a plugin](/plugins/register)
