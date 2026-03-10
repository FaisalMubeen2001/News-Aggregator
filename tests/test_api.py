from unittest.mock import patch, MagicMock
from backend.services.ai_service import summarize_article, analyze_sentiment, enrich_article


@patch("backend.services.ai_service.client")
def test_summarize_article(mock_client):
    mock_client.chat.completions.create.return_value = MagicMock(
        choices=[MagicMock(message=MagicMock(content="This is a test summary."))]
    )
    result = summarize_article(title="Test Article", content="Test content.")
    assert result == "This is a test summary."


@patch("backend.services.ai_service.client")
def test_analyze_sentiment_positive(mock_client):
    mock_client.chat.completions.create.return_value = MagicMock(
        choices=[MagicMock(message=MagicMock(content="Positive"))]
    )
    result = analyze_sentiment(title="Great news!", description="Things are looking up.")
    assert result == "Positive"


@patch("backend.services.ai_service.client")
def test_analyze_sentiment_negative(mock_client):
    mock_client.chat.completions.create.return_value = MagicMock(
        choices=[MagicMock(message=MagicMock(content="Negative"))]
    )
    result = analyze_sentiment(title="Market crashes", description="Stocks hit a low.")
    assert result == "Negative"


@patch("backend.services.ai_service.client")
def test_analyze_sentiment_neutral(mock_client):
    mock_client.chat.completions.create.return_value = MagicMock(
        choices=[MagicMock(message=MagicMock(content="Neutral"))]
    )
    result = analyze_sentiment(title="New study released", description="Scientists publish research.")
    assert result == "Neutral"


@patch("backend.services.ai_service.client")
def test_enrich_article(mock_client):
    mock_client.chat.completions.create.return_value = MagicMock(
        choices=[MagicMock(message=MagicMock(content="This is a test summary."))]
    )
    result = enrich_article(title="Test", content="Content.", description="Description.")
    assert "summary" in result
    assert "sentiment" in result