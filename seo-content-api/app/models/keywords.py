from pydantic import BaseModel
from typing import List

class KeywordRequest(BaseModel):
    topic: str
    industry: str
    language: str

class KeywordResponse(BaseModel):
    seed_keywords: List[str]
    long_tail_keywords: List[str]
    questions: List[str]
    intent_classification: str # "informational" or "transactional" or description
