# Rust SDK

**Status:** Ready · **Package:** `mediacore_sdk` · **Path:** `sdk/rust`

Async client built for Tokio services.

## Install

From the MediaCore repository root (crates.io publish comes later):

::: code-group

```bash [cargo]
cargo add --path sdk/rust
```

```toml [Cargo.toml]
[dependencies]
mediacore_sdk = { path = "sdk/rust" }
```

:::

::: tip
Use a path dependency until `mediacore_sdk` is on crates.io.
:::

## Runtime

- Rust edition 2021
- Async (`tokio` + HTTP client)
- Errors via `mediacore_sdk::Result`

## Surface

| Method | HTTP |
|--------|------|
| `client.media().analyze(url)` | `POST /v1/analyze` |
| `client.media().download(url, format)` | `POST /v1/download` |
| `client.media().convert(path, options)` | `POST /v1/convert` |
| `client.media().thumbnail(url)` | `POST /v1/thumbnail` |
| `client.jobs().list(limit)` | `GET /v1/jobs` |
| `client.jobs().get(id)` | `GET /v1/jobs/{id}` |
| `client.plugins().list()` | `GET /v1/plugins` |

## Example

```rust
use mediacore_sdk::MediaCore;

#[tokio::main]
async fn main() -> mediacore_sdk::Result<()> {
    let client = MediaCore::new("dev-api-key-change-me");
    let meta = client.media().analyze("https://example.com/video.mp4").await?;
    let _job = client
        .media()
        .download("https://example.com/video.mp4", "original")
        .await?;
    let _jobs = client.jobs().list(50).await?;
    let _plugins = client.plugins().list().await?;
    println!("{meta}");
    Ok(())
}
```

## See also

- [REST API](/api/)
- [SDK overview](./)
