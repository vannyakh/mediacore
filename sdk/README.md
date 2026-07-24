# MediaCore SDKs

Thin HTTP clients for the permitted download API (`/v1/analyze`, `/v1/download`, jobs).

| Language | Install |
|----------|---------|
| **Python** | `pip install -e sdk/python` |
| **Node / npm** | `npm install ./sdk/javascript` |
| **TypeScript** | `npm install ./sdk/typescript` |
| **PHP** | `composer require mediacore/sdk:@dev` (path repo → `sdk/php`) |
| **Go** | `go get github.com/mediacore/sdk-go` (or local `replace`) |
| **Other** | Use REST + `curl` / any HTTP client — see [docs/sdk](../docs/sdk/) |

Start the API first:

```bash
uv run uvicorn apps.api.main:app --reload --port 8000
```

Dev API key: `dev-api-key-change-me`
