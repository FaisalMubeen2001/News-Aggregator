from backend.services.news_service import fetch_all_categories
from backend.services.ai_service import enrich_article
from backend.services.email_service import send_daily_digest


def fetch_and_enrich_articles():
    print("⏰ Scheduler: Fetching fresh articles...")
    articles = fetch_all_categories(page_size=3)
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
    print(f"✅ Scheduler: Fetched and enriched {len(enriched)} articles.")
    return enriched


def send_digest_job():
    print("📧 Scheduler: Preparing daily digest...")
    articles = fetch_and_enrich_articles()
    send_daily_digest(articles)