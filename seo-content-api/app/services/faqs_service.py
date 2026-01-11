import json
from app.models.faqs import FAQRequest, FAQResponse
from app.services.openai_service import client, deployment_name

def extract_faqs(request: FAQRequest) -> FAQResponse:
    system_prompt = """
    You are an expert content analyzer. distinct features:
    1. Extract relevant FAQs from the provided content.
    2. Answers should be concise (50-150 words).
    3. Generate a valid JSON-LD schema for FAQPage.
    4. Return valid JSON matching:
    {
        "faqs": [
            {"question": "Q1", "answer": "A1"}
        ],
        "json_ld_schema": {
            "@context": "https://schema.org",
            "@type": "FAQPage",
            "mainEntity": [
                {
                    "@type": "Question",
                    "name": "Q1",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "A1"
                    }
                }
            ]
        }
    }
    """

    user_prompt = f"""
    Content: {request.article_content}
    Max Questions: {request.max_questions}
    """

    try:
        response = client.chat.completions.create(
            model=deployment_name,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            response_format={"type": "json_object"},
            temperature=0.5
        )
        
        content = response.choices[0].message.content
        data = json.loads(content)
        return FAQResponse(**data)
    except Exception as e:
        print(f"Error in extract_faqs: {e}")
        raise e
