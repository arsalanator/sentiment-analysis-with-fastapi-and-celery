from celery import Celery
from core.application.use_cases.sentiment_csv_use_case import SentimentCSVUseCase
from core.infrastructure.adapters.output.textblob_adapter.textblob_sentiment_classifier import TextBlobSentimentClassifier
from core.infrastructure.adapters.output.pandas_adapter.local_file_repository import LocalFileRepository

app = Celery("tasks", broker="redis://localhost:6379/0")

classifier = TextBlobSentimentClassifier()
file_repo = LocalFileRepository()
use_case = SentimentCSVUseCase(classifier, file_repo)


@app.task(bind=True)
def process_csv(self, file_path: str):
    try:
        return use_case.analyze_csv(file_path)
    except Exception as e:
        self.retry(exc=e, countdown=5, max_retries=3)
