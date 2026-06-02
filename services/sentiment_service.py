from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

def get_score(text):
    return analyzer.polarity_scores(text)["compound"]