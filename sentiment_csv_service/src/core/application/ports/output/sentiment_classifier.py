from abc import ABC, abstractmethod
from src.core.domain.models.comment import Comment


class SentimentClassifier(ABC):
    @abstractmethod
    def classify(self, comment: Comment) -> Comment:
        """Assign sentiment to the comment."""
        pass
