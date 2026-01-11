from pydantic import BaseModel
from typing import List, Optional

class ArticleRequest(BaseModel):
    main_keyword: str
    secondary_keywords: List[str]
    word_count: int = 1000
    tone: str = "professional"

class ArticleSection(BaseModel):
    heading: str
    content: str
    subsections: Optional[List['ArticleSection']] = None

class ArticleResponse(BaseModel):
    title: str
    sections: List[ArticleSection]
    keyword_density: float
    call_to_actions: List[str]
