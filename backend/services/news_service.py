import requests
from datetime import datetime
from backend.models.article import Article
from backend.config import NEWS_API_KEY

BASE_URL = "https://newsapi.org/v2"

CATEGORIES = ["business", "technology", "sports", "health", "science", "entertainment"]


def fetch_articles(category: str = "technology", page_size: int = 10) -> list[Article]:
    url = f"{BASE_URL}/top-headlines"
    params = {
        "category": category,
        "pageSize": page_size,
        "language": "en",
        "apiKey": NEWS_API_KEY,
    }

    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()

    articles = []
    for item in data.get("articles", []):
        try:
            article = Article(
                title=item["title"],
                description=item.get("description"),
                content=item.get("content"),
                url=item["url"],
                source=item["source"]["name"],
                published_at=datetime.fromisoformat(
                    item["publishedAt"].replace("Z", "+00:00")
                ),
                category=category,
            )
            articles.append(article)
        except Exception as e:
            print(f"Skipping article due to error: {e}")
            continue

    return articles


def fetch_all_categories(page_size: int = 5) -> list[Article]:
    all_articles = []
    for category in CATEGORIES:
        articles = fetch_articles(category=category, page_size=page_size)
        all_articles.extend(articles)
    return all_articles