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

    name = name.strip()
    if not name:
        return jsonify({"error": "Please enter a country name"}), 400

    geo = get_country(name)

    if not geo:
        return jsonify({"error": "Country not found. Try a different spelling."}), 404

    news = get_news(name)

    if not news:
        sentiment = 0
        sentiment_label = "Neutral"
    else:
        sentiment = sum([get_score(n) for n in news]) / len(news)
        sentiment = round(sentiment, 2)
        if sentiment > 0.1:
            sentiment_label = "Positive 😊"
        elif sentiment < -0.1:
            sentiment_label = "Negative 😟"
        else:
            sentiment_label = "Neutral 😐"

    return jsonify({
        "country": geo["name"],
        "flag": geo["flag"],
        "lat": geo["lat"],
        "lon": geo["lon"],
        "sentiment": sentiment,
        "sentiment_label": sentiment_label,
        "articles": news,
        "no_news": len(news) == 0
    })


if __name__ == "__main__":
    app.run(debug=True)