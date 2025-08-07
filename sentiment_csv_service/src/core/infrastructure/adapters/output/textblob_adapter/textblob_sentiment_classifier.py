from textblob import TextBlob
from core.application.ports.output.sentiment_classifier import SentimentClassifier
from core.domain.models.comment import Comment, Sentiment


class TextBlobSentimentClassifier(SentimentClassifier):
    def classify(self, comment: Comment) -> Comment:
        polarity = TextBlob(comment.text).sentiment.polarity
        if polarity > 0.1:
            comment.sentiment = Sentiment.POSITIVE
        elif polarity < -0.1:
            comment.sentiment = Sentiment.NEGATIVE
        else:
            comment.sentiment = Sentiment.NEUTRAL
        return comment
