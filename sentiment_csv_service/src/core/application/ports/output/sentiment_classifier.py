from abc import ABC, abstractmethod
from core.domain.models.comment import Comment


class SentimentClassifier(ABC):
    @abstractmethod
    def classify(self, comment: Comment) -> Comment:
        pass
