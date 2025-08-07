from abc import ABC, abstractmethod
from typing import BinaryIO


class FileRepository(ABC):
    @abstractmethod
    def save_uploaded_file(self, file_stream: BinaryIO, filename: str) -> str:
        """Save the uploaded file and return the stored path."""
        pass

    @abstractmethod
    def get_file_path(self, filename: str) -> str:
        """Return the path to the stored file."""
        pass
