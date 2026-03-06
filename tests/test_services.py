from unittest.mock import patch, MagicMock
from datetime import datetime
from backend.services.news_service import fetch_articles, fetch_all_categories


MOCK_RESPONSE = {
    "articles": [
        {
            "title": "Test Article",
            "description": "Test Description",
            "content": "Test Content",
            "url": "https://test.com/article",
            "source": {"name": "Test Source"},
            "publishedAt": "2026-03-06T12:00:00Z",
        }
    ]
}


@patch("backend.services.news_service.requests.get")
def test_fetch_articles_returns_list(mock_get):
    mock_get.return_value = MagicMock(
        status_code=200,
        json=lambda: MOCK_RESPONSE
    )
    mock_get.return_value.raise_for_status = MagicMock()

    articles = fetch_articles(category="technology", page_size=1)

    assert isinstance(articles, list)
    assert len(articles) == 1
    assert articles[0].title == "Test Article"
    assert articles[0].category == "technology"


@patch("backend.services.news_service.requests.get")
def test_fetch_articles_handles_missing_fields(mock_get):
    mock_get.return_value = MagicMock(
        status_code=200,
        json=lambda: {"articles": [{"title": None, "url": None, "source": {"name": "X"}, "publishedAt": "2026-03-06T12:00:00Z"}]}
    )
    mock_get.return_value.raise_for_status = MagicMock()

    articles = fetch_articles(category="technology", page_size=1)
    assert isinstance(articles, list)


@patch("backend.services.news_service.fetch_articles")
def test_fetch_all_categories(mock_fetch):
    mock_fetch.return_value = [
        MagicMock(title="Article", category="technology")
    ]

    articles = fetch_all_categories(page_size=1)

    assert len(articles) == 6  # One per category