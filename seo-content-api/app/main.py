from fastapi import FastAPI
from app.routers import keywords, articles, metadata, faqs, social

app = FastAPI(title="SEO Content API", description="API for generating SEO optimized content using AI.")

app.include_router(keywords.router, prefix="/api/keywords", tags=["Keywords"])
app.include_router(articles.router, prefix="/api/articles", tags=["Articles"])
app.include_router(metadata.router, prefix="/api/metadata", tags=["Metadata"])
app.include_router(faqs.router, prefix="/api/faqs", tags=["FAQs"])
app.include_router(social.router, prefix="/api/social", tags=["Social Media"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the SEO Content API. Visit /docs for documentation."}
