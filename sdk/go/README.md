# MediaCore Go SDK

## Install

```bash
# from your Go module
go get github.com/mediacore/sdk-go@latest

# or local replace during development
# go.mod:
# replace github.com/mediacore/sdk-go => ../mediacore/sdk/go
go mod edit -replace=github.com/mediacore/sdk-go=./sdk/go
go get github.com/mediacore/sdk-go@v0.0.0
```

## Usage

```go
package main

import (
	"fmt"
	"time"

	mediacore "github.com/mediacore/sdk-go"
)

func main() {
	c := mediacore.New("dev-api-key-change-me", "http://localhost:8000")
	meta, err := c.Media.Analyze("https://example.com/video.mp4")
	if err != nil {
		panic(err)
	}
	url, _ := meta["url"].(string)
	job, err := c.Media.Download(url, "original")
	if err != nil {
		panic(err)
	}
	done, err := c.Jobs.Wait(job["job_id"].(string), 2*time.Minute)
	if err != nil {
		panic(err)
	}
	fmt.Println(done["status"], done["result_path"])
}
```
