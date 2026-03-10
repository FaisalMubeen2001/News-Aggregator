from fastapi import FastAPI, Query
from contextlib import asynccontextmanager
from backend.services.news_service import fetch_articles, fetch_all_categories, CATEGORIES
from backend.services.ai_service import enrich_article
from backend.scheduler.scheduler import start_scheduler, stop_scheduler


@asynccontextmanager
async def lifespan(app: FastAPI):
    start_scheduler()
    yield
    stop_scheduler()


app = FastAPI(
    title="News Aggregator API",
    version="1.0.0",
    description="Fetches, summarizes and aggregates news articles",
    lifespan=lifespan
)


@app.get("/")
def root():
    return {"message": "Welcome to News Aggregator API", "version": "1.0.0"}


@app.get("/articles")
def get_articles(
    category: str = Query(default="technology", enum=CATEGORIES),
    page_size: int = Query(default=5, ge=1, le=20),
    enrich: bool = Query(default=False)
):
    articles = fetch_articles(category=category, page_size=page_size)

    if enrich:
        enriched = []
        for article in articles:
            result = enrich_article(
                title=article.title,
                content=article.content,
                description=article.description
            )
            article.summary = result["summary"]
            article.sentiment = result["sentiment"]
            enriched.append(article)
        articles = enriched

    return {"category": category, "total": len(articles), "articles": articles}


@app.get("/articles/all")
def get_all_articles(page_size: int = Query(default=3, ge=1, le=10)):
    articles = fetch_all_categories(page_size=page_size)
    return {"total": len(articles), "articles": articles}

@app.get("/test-email")
def test_email():
    from backend.services.news_service import fetch_articles
    from backend.services.email_service import send_daily_digest
    articles = fetch_articles(category="technology", page_size=3)
    success = send_daily_digest(articles)
    return {"success": success}

@app.get("/categories")
def get_categories():
    return {"categories": CATEGORIES}