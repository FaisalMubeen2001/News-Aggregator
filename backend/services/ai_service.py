from groq import Groq
from backend.config import GROQ_API_KEY

client = Groq(api_key=GROQ_API_KEY)
MODEL = "llama-3.3-70b-versatile"


def summarize_article(title: str, content: str) -> str:
    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {
                    "role": "system",
                    "content": "You are a news summarizer. Summarize articles in 2-3 concise sentences. Return only the summary, no extra text."
                },
                {
                    "role": "user",
                    "content": f"Title: {title}\nContent: {content}"
                }
            ],
            max_tokens=200
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"Summarization error: {e}")
        return None


def analyze_sentiment(title: str, description: str) -> str:
    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {
                    "role": "system",
                    "content": "You are a sentiment analyzer. Reply with only one word: Positive, Negative, or Neutral."
                },
                {
                    "role": "user",
                    "content": f"Title: {title}\nDescription: {description}"
                }
            ],
            max_tokens=10
        )
        sentiment = response.choices[0].message.content.strip().lower()
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