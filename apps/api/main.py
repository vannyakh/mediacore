"""MediaCore API entrypoint."""

from __future__ import annotations

import logging
from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from starlette.responses import Response

from apps.api.config import get_settings
from apps.api.db.session import init_db
from apps.api.middleware.logging import RequestLoggingMiddleware
from apps.api.routes import health, v1
from mediacore import __version__
from packages.logging.setup import setup_logging
from packages.telemetry.metrics import render_metrics

setup_logging()


@asynccontextmanager
async def lifespan(_app: FastAPI):
    init_db()
    yield


def create_app() -> FastAPI:
    settings = get_settings()
    app = FastAPI(
        title=settings.app_name,
        version=__version__,
        description="MediaCore — media extraction, processing, and automation platform",
        lifespan=lifespan,
    )

    origins = [o.strip() for o in settings.cors_origins.split(",") if o.strip()]
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins if origins != ["*"] else ["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.add_middleware(RequestLoggingMiddleware)

    app.include_router(health.router)
    app.include_router(v1.router)

    # Back-compat aliases under /api/v1
    app.include_router(v1.router, prefix="/api")

    storage_root = Path(settings.storage_root)
    storage_root.mkdir(parents=True, exist_ok=True)
    app.mount("/files", StaticFiles(directory=str(storage_root)), name="files")

    @app.get("/metrics")
    def metrics() -> Response:
        body, content_type = render_metrics()
        return Response(body, media_type=content_type)

    return app


app = create_app()


def run() -> None:
    import uvicorn

    uvicorn.run("apps.api.main:app", host="0.0.0.0", port=8000, reload=False)


if __name__ == "__main__":
    run()
