from unittest.mock import patch, MagicMock
from backend.services.ai_service import summarize_article, analyze_sentiment, enrich_article


@patch("backend.services.ai_service.client")
def test_summarize_article(mock_client):
    mock_client.models.generate_content.return_value = MagicMock(
        text="This is a test summary of the article."
    )

    result = summarize_article(
        title="Test Article",
        content="This is the content of the test article."
    )

    assert result == "This is a test summary of the article."
    mock_client.models.generate_content.assert_called_once()


@patch("backend.services.ai_service.client")
def test_analyze_sentiment_positive(mock_client):
    mock_client.models.generate_content.return_value = MagicMock(text="Positive")

    result = analyze_sentiment(
        title="Great news for everyone!",
        description="Things are looking up."
    )

    assert result == "Positive"


@patch("backend.services.ai_service.client")
def test_analyze_sentiment_negative(mock_client):
    mock_client.models.generate_content.return_value = MagicMock(text="Negative")

    result = analyze_sentiment(
        title="Market crashes worldwide",
        description="Stocks hit an all time low."
    )

    assert result == "Negative"


@patch("backend.services.ai_service.client")
def test_analyze_sentiment_neutral(mock_client):
    mock_client.models.generate_content.return_value = MagicMock(text="Neutral")

    result = analyze_sentiment(
        title="Scientists publish new research",
        description="A new study was released today."
    )

    assert result == "Neutral"


@patch("backend.services.ai_service.client")
def test_enrich_article(mock_client):
    mock_client.models.generate_content.return_value = MagicMock(
        text="This is a test summary."
    )

    result = enrich_article(
        title="Test Article",
        content="Test content.",
        description="Test description."
    )

    assert "summary" in result
    assert "sentiment" in result
    assert result["summary"] == "This is a test summary."