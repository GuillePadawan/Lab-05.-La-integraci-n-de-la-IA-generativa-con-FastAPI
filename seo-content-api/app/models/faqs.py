from pydantic import BaseModel
from typing import List, Dict, Any

class FAQRequest(BaseModel):
    article_content: str
    max_questions: int = 5

class FAQ(BaseModel):
    question: str
    answer: str

class FAQResponse(BaseModel):
    faqs: List[FAQ]
    json_ld_schema: Dict[str, Any]
