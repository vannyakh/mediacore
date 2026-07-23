from fastapi import APIRouter, Depends, HTTPException, status

from apps.api.config import get_settings
from apps.api.db.models import ApiKey
from apps.api.middleware.auth import require_api_key
from apps.api.schemas import AnalyzeRequest, AnalyzeResponse, FormatOut
from extractor.core.engine import ExtractorEngine
from extractor.core.exceptions import ExtractorError

router = APIRouter(prefix="/api/v1", tags=["analyze"])


@router.post("/analyze", response_model=AnalyzeResponse)
def analyze(body: AnalyzeRequest, _: ApiKey = Depends(require_api_key)) -> AnalyzeResponse:
    settings = get_settings()
    engine = ExtractorEngine()
    try:
        meta = engine.analyze(body.url, allow_private=settings.allow_private_urls)
    except ExtractorError as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail={
            "error": exc.message,
            "code": exc.code,
        }) from exc

    return AnalyzeResponse(
        platform=meta.platform,
        title=meta.title,
        duration=meta.duration,
        thumbnail=meta.thumbnail,
        description=meta.description,
        author=meta.author,
        url=meta.url,
        formats=[FormatOut(**f.to_dict()) for f in meta.formats],
    )
