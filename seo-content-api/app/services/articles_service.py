import json
from app.models.articles import ArticleRequest, ArticleResponse
from app.services.openai_service import client, deployment_name

def generate_article(request: ArticleRequest) -> ArticleResponse:
    system_prompt = """
    You are an expert SEO content writer. Write a comprehensive article based on the provided keywords.
    Follow these rules:
    1. Structure the content with a clear Title (H1), main sections (H2), and subsections (H3).
    2. Ensure natural keyword integration. Avoid keyword stuffing.
    3. Include relevant Call to Actions (CTAs).
    4. Return the result as a JSON object strictly matching this schema:
    {
        "title": "The H1 Title",
        "sections": [
            {
                "heading": "H2 Heading",
                "content": "The content paragraph...",
                "subsections": [
                    { "heading": "H3 Heading", "content": "The content..." }
                ]
            }
        ],
        "keyword_density": 1.5,
        "call_to_actions": ["CTA 1", "CTA 2"]
    }
    The keyword_density should be a float representing the percentage of the main keyword usage.
    """

    user_prompt = f"""
    Main Keyword: {request.main_keyword}
    Secondary Keywords: {', '.join(request.secondary_keywords)}
    Approximate Word Count: {request.word_count}
    Tone: {request.tone}
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
        # Handle potentially missing subsections or empty lists to make Pydantic happy if needed, 
        # but the prompt asks for strict schema.
        return ArticleResponse(**data)
    except Exception as e:
        print(f"Error in generate_article: {e}")
        raise e
