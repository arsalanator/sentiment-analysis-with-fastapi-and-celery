from core.application.ports.input.sentiment_analysis_service import SentimentAnalysisService
from core.application.ports.output.sentiment_classifier import SentimentClassifier
from core.application.ports.output.csv_processor import CSVProcessor


class SentimentCSVUseCase(SentimentAnalysisService):
    def __init__(self, classifier: SentimentClassifier, csv_processor: CSVProcessor):
        self.classifier = classifier
        self.csv_processor = csv_processor

    def analyze_csv(self, file_path: str) -> str:
        comments = self.csv_processor.read_comments(file_path)
        for comment in comments:
            self.classifier.classify(comment)
        return self.csv_processor.write_comments(comments, "processed_" + file_path.split("/")[-1])
