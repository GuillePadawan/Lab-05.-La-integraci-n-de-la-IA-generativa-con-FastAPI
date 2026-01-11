import json
from app.models.keywords import KeywordRequest, KeywordResponse
from app.services.openai_service import client, deployment_name

def generate_keywords(request: KeywordRequest) -> KeywordResponse:
    system_prompt = """
    You are an expert SEO specialist. 
    Generate a list of keywords based on the user's topic, industry, and language.
    Classify the intent as either "informational" or "transactional".
    Return the response in strictly valid JSON format matching the following structure:
    {
        "seed_keywords": ["keyword1", "keyword2"],
        "long_tail_keywords": ["long tail keyword 1", ...],
        "questions": ["question 1?", ...],
        "intent_classification": "informational" or "transactional"
    }
    """
    
    user_prompt = f"""
    Topic: {request.topic}
    Industry: {request.industry}
    Language: {request.language}
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
        return KeywordResponse(**data)
    except Exception as e:
        print(f"Error in generate_keywords: {e}")
        # In a real app, you might want to raise a specific HTTP exception or handle retry
        raise e
