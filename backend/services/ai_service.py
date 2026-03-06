from google import genai
from backend.config import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)


def summarize_article(title: str, content: str) -> str:
    try:
        prompt = f"""
        Summarize the following news article in 2-3 concise sentences.
        Only return the summary, no extra text.

        Title: {title}
        Content: {content}
        """
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )
        return response.text.strip()
    except Exception as e:
        print(f"Summarization error: {e}")
        return None


def analyze_sentiment(title: str, description: str) -> str:
    try:
        prompt = f"""
        Analyze the sentiment of the following news article.
        Reply with only one word: Positive, Negative, or Neutral.

        Title: {title}
        Description: {description}
        """
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )
        sentiment = response.text.strip().lower()
        if "positive" in sentiment:
            return "Positive"
        elif "negative" in sentiment:
            return "Negative"
        else:
            return "Neutral"
    except Exception as e:
        print(f"Sentiment analysis error: {e}")
        return None


def enrich_article(title: str, content: str, description: str) -> dict:
    summary = summarize_article(title, content or description)
    sentiment = analyze_sentiment(title, description or content)
    return {"summary": summary, "sentiment": sentiment}