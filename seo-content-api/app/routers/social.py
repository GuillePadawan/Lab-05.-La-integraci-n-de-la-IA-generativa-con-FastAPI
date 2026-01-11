from fastapi import APIRouter, HTTPException
from app.models.social import SocialRequest, SocialResponse
from app.services.social_service import generate_social_media

router = APIRouter()

@router.post("/summaries", response_model=SocialResponse)
async def create_social_summaries(request: SocialRequest):
    try:
        return generate_social_media(request)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
