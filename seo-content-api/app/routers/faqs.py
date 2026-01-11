from fastapi import APIRouter, HTTPException
from app.models.faqs import FAQRequest, FAQResponse
from app.services.faqs_service import extract_faqs

router = APIRouter()

@router.post("/extract", response_model=FAQResponse)
async def create_faqs(request: FAQRequest):
    try:
        return extract_faqs(request)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
