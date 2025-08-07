from abc import ABC, abstractmethod
from src.core.domain.models.comment import Comment


class SentimentAnalysisRepository(ABC):
    @abstractmethod
    def analyze(self, comment: Comment) -> Comment:
        """
        Analyze the sentiment of a comment and return the comment with updated sentiment.
        """
        pass
