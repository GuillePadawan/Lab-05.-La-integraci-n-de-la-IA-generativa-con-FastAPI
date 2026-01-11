from fastapi import APIRouter, HTTPException
from app.models.metadata import MetadataRequest, MetadataResponse
from app.services.metadata_service import generate_metadata

router = APIRouter()

@router.post("/generate", response_model=MetadataResponse)
async def create_metadata(request: MetadataRequest):
    try:
        return generate_metadata(request)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
