from fastapi import APIRouter, HTTPException
from app.models.keywords import KeywordRequest, KeywordResponse
from app.services.keywords_service import generate_keywords

router = APIRouter()

@router.post("/generate", response_model=KeywordResponse)
async def create_keywords(request: KeywordRequest):
    try:
        return generate_keywords(request)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
