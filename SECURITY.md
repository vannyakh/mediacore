# Security policy

## Supported versions

| Version | Supported |
|---------|-----------|
| `0.1.x` (main) | Yes |
| Older pre-releases | Best effort |

## Reporting a vulnerability

Please **do not** open a public GitHub issue for security problems.

Prefer a private report to the maintainers (GitHub Security Advisories when enabled, or contact listed on the project organization page).

Include:

- Description and impact
- Steps to reproduce / PoC (if safe)
- Affected versions / commit
- Suggested fix (optional)

We aim to acknowledge reports within a few business days.

## Scope notes

- MediaCore providers must use official/permitted APIs. Reports about “bypassing” platform access controls are out of scope for product features and will not be implemented.
- Secrets in `.env` and API keys are operator responsibilities; do not commit them.
