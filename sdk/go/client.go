package mediacore

import (
	"bytes"
	"encoding/json"
	"fmt"
	"io"
	"net/http"
	"strings"
	"time"
)

// Client is the MediaCore Go SDK for the permitted download API.
type Client struct {
	BaseURL    string
	APIKey     string
	HTTPClient *http.Client

	Media     *MediaAPI
	Jobs      *JobsAPI
	Providers *ProvidersAPI
	Plugins   *PluginsAPI
}

func New(apiKey string, baseURL ...string) *Client {
	base := "http://localhost:8000"
	if len(baseURL) > 0 && baseURL[0] != "" {
		base = strings.TrimRight(baseURL[0], "/")
	}
	c := &Client{
		BaseURL: base,
		APIKey:  apiKey,
		HTTPClient: &http.Client{
			Timeout: 60 * time.Second,
		},
	}
	c.Media = &MediaAPI{c: c}
	c.Jobs = &JobsAPI{c: c}
	c.Providers = &ProvidersAPI{c: c}
	c.Plugins = &PluginsAPI{c: c}
	return c
}

func (c *Client) request(method, path string, body any, out any) error {
	var reader io.Reader
	if body != nil {
		raw, err := json.Marshal(body)
		if err != nil {
			return err
		}
		reader = bytes.NewReader(raw)
	}
	req, err := http.NewRequest(method, c.BaseURL+path, reader)
	if err != nil {
		return err
	}
	req.Header.Set("Content-Type", "application/json")
	req.Header.Set("X-API-Key", c.APIKey)
	res, err := c.HTTPClient.Do(req)
	if err != nil {
		return err
	}
	defer res.Body.Close()
	data, err := io.ReadAll(res.Body)
	if err != nil {
		return err
	}
	if res.StatusCode >= 400 {
		return fmt.Errorf("API %d: %s", res.StatusCode, string(data))
	}
	if out == nil || len(data) == 0 {
		return nil
	}
	return json.Unmarshal(data, out)
}

type MediaAPI struct{ c *Client }

func (m *MediaAPI) Analyze(url string) (map[string]any, error) {
	var out map[string]any
	err := m.c.request("POST", "/v1/analyze", map[string]string{"url": url}, &out)
	return out, err
}

func (m *MediaAPI) Download(url string, format string) (map[string]any, error) {
	if format == "" {
		format = "original"
	}
	var out map[string]any
	err := m.c.request("POST", "/v1/download", map[string]string{"url": url, "format": format}, &out)
	return out, err
}

type JobsAPI struct{ c *Client }

func (j *JobsAPI) Get(id string) (map[string]any, error) {
	var out map[string]any
	err := j.c.request("GET", "/v1/jobs/"+id, nil, &out)
	return out, err
}

func (j *JobsAPI) Wait(id string, timeout time.Duration) (map[string]any, error) {
	if timeout <= 0 {
		timeout = 120 * time.Second
	}
	deadline := time.Now().Add(timeout)
	var last map[string]any
	for time.Now().Before(deadline) {
		out, err := j.Get(id)
		if err != nil {
			return nil, err
		}
		last = out
		status, _ := out["status"].(string)
		if status == "completed" || status == "failed" || status == "cancelled" {
			return out, nil
		}
		time.Sleep(500 * time.Millisecond)
	}
	return last, fmt.Errorf("job %s did not finish within %s", id, timeout)
}

type ProvidersAPI struct{ c *Client }

func (p *ProvidersAPI) List() ([]map[string]any, error) {
	var out []map[string]any
	err := p.c.request("GET", "/v1/providers", nil, &out)
	return out, err
}

type PluginsAPI struct{ c *Client }

func (p *PluginsAPI) List() ([]map[string]any, error) {
	var out []map[string]any
	err := p.c.request("GET", "/v1/plugins", nil, &out)
	return out, err
}
