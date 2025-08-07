import os
import uuid
import pandas as pd
from typing import List
from core.application.ports.output.csv_processor import CSVProcessor
from core.domain.models.comment import Comment, Sentiment


class PandasCSVProcessor(CSVProcessor):
    def __init__(self, storage_dir="data"):
        self.storage_dir = storage_dir
        os.makedirs(self.storage_dir, exist_ok=True)

    def read_comments(self, file_path: str) -> List[Comment]:
        df = pd.read_csv(file_path)
        comments = []
        for _, row in df.iterrows():
            comment_text = row.get("comment") or row.get("text")
            if comment_text is None:
                continue  # Skip row if no comment field

            comments.append(Comment(
                id=str(uuid.uuid4()),
                text=str(comment_text).strip(),
                sentiment=Sentiment.UNKNOWN
            ))
        return comments

    def write_comments(self, comments: List[Comment], file_name: str) -> str:
        df = pd.DataFrame([
            {
                "id": c.id,
                "comment": c.text,
                "sentiment": c.sentiment.value
            } for c in comments
        ])
        path = os.path.join(self.storage_dir, file_name)
        df.to_csv(path, index=False)
        return path
