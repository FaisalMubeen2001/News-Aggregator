import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from backend.config import EMAIL_SENDER, EMAIL_PASSWORD, EMAIL_RECEIVER


def send_daily_digest(articles: list) -> bool:
    try:
        msg = MIMEMultipart("alternative")
        msg["Subject"] = "📰 Your Daily News Digest"
        msg["From"] = EMAIL_SENDER
        msg["To"] = EMAIL_RECEIVER

        html = """
        <html>
        <body style="font-family: Arial, sans-serif; max-width: 700px; margin: auto; padding: 20px;">
            <h1 style="color: #3b82f6;">📰 Your Daily News Digest</h1>
            <p style="color: #6b7280;">Here are today's top stories:</p>
            <hr style="border: 1px solid #e5e7eb;">
        """

        for article in articles:
            sentiment_color = {
                "Positive": "#16a34a",
                "Negative": "#dc2626",
                "Neutral": "#6b7280"
            }.get(article.sentiment, "#6b7280")

            html += f"""
            <div style="margin: 20px 0; padding: 15px; border-radius: 10px; border: 1px solid #e5e7eb;">
                <p style="margin: 0 0 5px 0; font-size: 12px; color: #3b82f6; font-weight: bold; text-transform: uppercase;">{article.source}</p>
                <h2 style="margin: 0 0 10px 0; font-size: 16px; color: #1f2937;">{article.title}</h2>
                {f'<p style="margin: 0 0 10px 0; font-size: 14px; color: #4b5563;">{article.summary}</p>' if article.summary else ''}
                {f'<span style="font-size: 12px; font-weight: bold; color: {sentiment_color};">● {article.sentiment}</span>' if article.sentiment else ''}
                <br>
                <a href="{article.url}" style="font-size: 12px; color: #3b82f6;">Read more →</a>
            </div>
            """

        html += """
            <hr style="border: 1px solid #e5e7eb;">
            <p style="color: #9ca3af; font-size: 12px; text-align: center;">News Aggregator — Your daily AI-powered news digest</p>
        </body>
        </html>
        """

        msg.attach(MIMEText(html, "html"))

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(EMAIL_SENDER, EMAIL_PASSWORD)
            server.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, msg.as_string())

        print("✅ Daily digest email sent successfully!")
        return True

    except Exception as e:
        print(f"Email error: {e}")
        return False