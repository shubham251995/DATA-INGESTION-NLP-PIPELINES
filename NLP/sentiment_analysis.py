from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

class SentimentAnalysis:
    def __init__(self):
        self.analyzer = SentimentIntensityAnalyzer()

    def analyze_sentiment(self, text):
        """Analyze sentiment of the provided text."""
        sentiment_score = self.analyzer.polarity_scores(text)
        if sentiment_score['compound'] >= 0.05:
            return "Positive"
        elif sentiment_score['compound'] <= -0.05:
            return "Negative"
        else:
            return "Neutral"
