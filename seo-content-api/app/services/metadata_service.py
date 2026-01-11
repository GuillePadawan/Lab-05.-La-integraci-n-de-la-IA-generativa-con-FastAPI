import json
from app.models.metadata import MetadataRequest, MetadataResponse
from app.services.openai_service import client, deployment_name

def generate_metadata(request: MetadataRequest) -> MetadataResponse:
    system_prompt = """
    You are an SEO expert. Generate optimized meta titles and meta descriptions for the given article info.
    Rules:
    1. Generate 3 to 5 variants for each.
    2. Meta Titles must be under 60 characters.
    3. Meta Descriptions must be under 160 characters.
    4. Include the main keyword.
    5. Use persuasive language to improve CTR.
    6. Return a JSON object strictly matching this schema:
    {
        "meta_titles": [
            {"title": "Variant 1", "character_count": 55},
            ...
        ],
        "meta_descriptions": [
            {"description": "Variant 1...", "character_count": 150},
            ...
        ]
    }
    """

    user_prompt = f"""
    Article Title: {request.article_title}
    Main Keyword: {request.main_keyword}
    Excerpt: {request.article_excerpt}
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
        return MetadataResponse(**data)
    except Exception as e:
        print(f"Error in generate_metadata: {e}")
        raise e
