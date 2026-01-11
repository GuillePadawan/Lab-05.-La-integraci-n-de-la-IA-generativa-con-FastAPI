from pydantic import BaseModel
from typing import List

class MetadataRequest(BaseModel):
    article_title: str
    main_keyword: str
    article_excerpt: str

class MetaTitle(BaseModel):
    title: str
    character_count: int

class MetaDescription(BaseModel):
    description: str
    character_count: int

class MetadataResponse(BaseModel):
    meta_titles: List[MetaTitle]
    meta_descriptions: List[MetaDescription]
