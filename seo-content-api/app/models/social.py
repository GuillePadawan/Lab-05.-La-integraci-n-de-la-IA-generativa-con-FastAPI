from pydantic import BaseModel
from typing import List, Optional

class SocialRequest(BaseModel):
    article_title: str
    article_content: str
    target_platforms: List[str]

class TwitterContent(BaseModel):
    content: str
    hashtags: List[str]
    character_count: int

class LinkedInContent(BaseModel):
    content: str
    hashtags: List[str]

class InstagramContent(BaseModel):
    content: str
    hashtags: List[str]
    visual_suggestion: Optional[str] = None # Optional: Description for image

class FacebookContent(BaseModel):
    content: str
    hashtags: List[str]

class SocialResponse(BaseModel):
    twitter: Optional[TwitterContent] = None
    linkedin: Optional[LinkedInContent] = None
    instagram: Optional[InstagramContent] = None
    facebook: Optional[FacebookContent] = None
