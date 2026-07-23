# Gateway (Nginx)

Reverse proxy in front of the FastAPI service.

- Rate limiting via `limit_req_zone` (30 r/s, burst 60)
- Proxies `/api`, `/health`, `/metrics`, `/files`
- Compose maps host `8080` → nginx `80`

Tune limits in `nginx.conf` for production.
