from abc import ABC, abstractmethod


class FileRepository(ABC):
    @abstractmethod
    def save(self, content: str, filename: str) -> str:
        pass

    @abstractmethod
    def load(self, file_path: str) -> str:
        pass