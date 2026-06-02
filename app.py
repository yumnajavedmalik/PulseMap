from flask import Flask, render_template, jsonify
from services.country_service import get_country
from services.news_service import get_news
from services.sentiment_service import get_score

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/country/<name>")
def country_api(name):

    geo = get_country(name)

    if not geo:
        return jsonify({
            "error": "Country not found"
        }), 404

    news = get_news(name)

    if not news:
        sentiment = 0
    else:
        sentiment = sum([get_score(n) for n in news]) / len(news)

    return jsonify({
        "country": geo["name"],
        "lat": geo["lat"],
        "lon": geo["lon"],
        "sentiment": round(sentiment, 2),
        "articles": news
    })


if __name__ == "__main__":
    app.run(debug=True)