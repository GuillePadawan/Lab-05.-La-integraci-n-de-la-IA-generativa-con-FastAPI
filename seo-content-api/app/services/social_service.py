import json
from app.models.social import SocialRequest, SocialResponse
from app.services.openai_service import client, deployment_name

def generate_social_media(request: SocialRequest) -> SocialResponse:
    platforms_str = ", ".join(request.target_platforms)
    
    system_prompt = f"""
    You are a social media manager. Generate posts for the following platforms: {platforms_str}.
    Based on the article provided.
    
    Rules:
    - Twitter/X: Max 280 chars. Concise, punchy.
    - LinkedIn: Professional tone, longer format.
    - Instagram: Engaging, visual-oriented text. Include a visual suggestion description.
    - Facebook: Conversational, community-focused.
    - Include relevant hashtags for each.
    
    Return a JSON object. Keys should be lowercase platform names (twitter, linkedin, instagram, facebook).
    If a platform is not requested, do not include it or include it as null.
    
    Schema example:
    {{
        "twitter": {{ "content": "...", "hashtags": ["tag1"], "character_count": 100 }},
        "linkedin": {{ "content": "...", "hashtags": ["tag1"] }},
        "instagram": {{ "content": "...", "hashtags": ["tag1"], "visual_suggestion": "Image of..." }},
        "facebook": {{ "content": "...", "hashtags": ["tag1"] }}
    }}
    """

    user_prompt = f"""
    Title: {request.article_title}
    Content Summary: {request.article_content[:2000]}... (truncated)
    Target Platforms: {request.target_platforms}
    """

    try:
        response = client.chat.completions.create(
            model=deployment_name,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            response_format={"type": "json_object"},
            temperature=0.7
        )
        
        content = response.choices[0].message.content
        data = json.loads(content)
        return SocialResponse(**data)
    except Exception as e:
        print(f"Error in generate_social_media: {e}")
        raise e
