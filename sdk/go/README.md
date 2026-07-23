# Go SDK (stub)

```go
package apidownloader

// Client is a minimal HTTP client stub for the REST API.
type Client struct {
    BaseURL string
    APIKey  string
}

// Analyze POST /api/v1/analyze
func (c *Client) Analyze(url string) (map[string]any, error) {
    panic("not implemented — use REST directly or contribute the Go client")
}
```
