from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()


def get_score(article):
    text = article["title"] if isinstance(article, dict) else article
    return analyzer.polarity_scores(text)["compound"]