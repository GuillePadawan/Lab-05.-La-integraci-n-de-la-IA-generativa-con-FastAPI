from fastapi import APIRouter, HTTPException
from app.models.articles import ArticleRequest, ArticleResponse
from app.services.articles_service import generate_article

router = APIRouter()

@router.post("/generate", response_model=ArticleResponse)
async def create_article(request: ArticleRequest):
    try:
        return generate_article(request)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
