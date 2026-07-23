from fastapi import APIRouter, Depends

from apps.api.db.models import ApiKey
from apps.api.middleware.auth import require_api_key
from apps.api.schemas import PlatformOut
from extractor.core.engine import ExtractorEngine

router = APIRouter(prefix="/api/v1", tags=["platforms"])


@router.get("/platforms", response_model=list[PlatformOut])
def list_platforms(_: ApiKey = Depends(require_api_key)) -> list[PlatformOut]:
    engine = ExtractorEngine()
    return [PlatformOut(**p) for p in engine.platforms()]
