from fastapi import FastAPI, Query
from backend.services.news_service import fetch_articles, fetch_all_categories, CATEGORIES

app = FastAPI(
    title="News Aggregator API",
    version="1.0.0",
    description="Fetches, summarizes and aggregates news articles"
)


@app.get("/")
def root():
    return {"message": "Welcome to News Aggregator API", "version": "1.0.0"}


@app.get("/articles")
def get_articles(
    category: str = Query(default="technology", enum=CATEGORIES),
    page_size: int = Query(default=10, ge=1, le=50)
):
    articles = fetch_articles(category=category, page_size=page_size)
    return {"category": category, "total": len(articles), "articles": articles}


@app.get("/articles/all")
def get_all_articles(page_size: int = Query(default=5, ge=1, le=20)):
    articles = fetch_all_categories(page_size=page_size)
    return {"total": len(articles), "articles": articles}


@app.get("/categories")
def get_categories():
    return {"categories": CATEGORIES}