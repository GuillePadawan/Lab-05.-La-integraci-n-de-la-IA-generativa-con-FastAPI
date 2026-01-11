from openai import AzureOpenAI
from app.config import settings

def get_openai_client():
    return AzureOpenAI(
        api_key=settings.AZURE_OPENAI_API_KEY,
        api_version=settings.OPENAI_API_VERSION,
        azure_endpoint=settings.AZURE_OPENAI_ENDPOINT
    )

client = get_openai_client()
deployment_name = settings.AZURE_OPENAI_DEPLOYMENT_NAME
