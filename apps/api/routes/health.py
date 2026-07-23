from fastapi import APIRouter

from apps.api.schemas import HealthResponse
from mediacore import __version__

router = APIRouter(tags=["health"])


@router.get("/health", response_model=HealthResponse)
def health() -> HealthResponse:
    return HealthResponse(status="ok", service="mediacore-api", version=__version__)
