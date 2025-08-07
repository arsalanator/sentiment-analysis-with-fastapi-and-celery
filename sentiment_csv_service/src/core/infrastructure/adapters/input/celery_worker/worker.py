from celery import Celery
from core.application.use_cases.sentiment_from_csv_use_case import SentimentCSVUseCase
from core.infrastructure.adapters.output.textblob_adapter.textblob_sentiment_classifier import TextBlobSentimentClassifier
from core.infrastructure.adapters.output.pandas_adapter.pandas_csv_processor import PandasCSVProcessor  # ✅ Correct class
from dotenv import load_dotenv
import os

load_dotenv()

CELERY_BROKER_URL = os.getenv("CELERY_BROKER_URL", "redis://localhost:6379/0")
CELERY_RESULT_BACKEND = os.getenv("CELERY_RESULT_BACKEND", "redis://localhost:6379/0")

app = Celery(
    "tasks",
    broker=CELERY_BROKER_URL,
    backend=CELERY_RESULT_BACKEND
)

classifier = TextBlobSentimentClassifier()
csv_processor = PandasCSVProcessor()  # ✅ Use the CSV adapter
use_case = SentimentCSVUseCase(classifier, csv_processor)

@app.task(name="process_csv", bind=True)
def process_csv(self, file_path: str):
    try:
        return use_case.analyze_csv(file_path)
    except Exception as e:
        self.retry(exc=e, countdown=5, max_retries=3)
