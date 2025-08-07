from abc import ABC, abstractmethod
from typing import List
from core.domain.models.comment import Comment


class CSVProcessor(ABC):
    @abstractmethod
    def read_comments(self, file_path: str) -> List[Comment]:
        pass

    @abstractmethod
    def write_comments(self, comments: List[Comment], file_name: str) -> str:
        pass
