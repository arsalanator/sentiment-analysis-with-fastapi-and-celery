from abc import ABC, abstractmethod


class SentimentAnalysisService(ABC):
    @abstractmethod
    def analyze_csv(self, file_path: str) -> str:
        pass
