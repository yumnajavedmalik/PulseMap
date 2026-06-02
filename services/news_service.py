import requests
import os
from dotenv import load_dotenv

load_dotenv()

GNEWS_API_KEY = os.getenv("GNEWS_API_KEY")


def get_news(country):
    try:
        if not GNEWS_API_KEY:
            return []

        url = (
            f"https://gnews.io/api/v4/search"
            f"?q={country}"
            f"&lang=en"
            f"&max=5"
            f"&token={GNEWS_API_KEY}"
        )

        r = requests.get(url, timeout=5)

        if r.status_code != 200:
            return []

        data = r.json()
        articles = data.get("articles", [])

        return [
            {"title": a["title"], "url": a["url"]}
            for a in articles
        ]

    except Exception:
        return []