import requests

GNEWS_API_KEY = "46b0639018ddca6cf09009957c5c0cc3"

def get_news(country):

    try:
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

        return [a["title"] for a in data.get("articles", [])]

    except:
        return []