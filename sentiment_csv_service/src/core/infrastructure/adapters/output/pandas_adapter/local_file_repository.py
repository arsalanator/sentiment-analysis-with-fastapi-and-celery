import os
from core.application.ports.output.file_repository import FileRepository


class LocalFileRepository(FileRepository):
    def __init__(self, storage_dir="data"):
        self.storage_dir = storage_dir
        os.makedirs(self.storage_dir, exist_ok=True)

    def save(self, content: str, filename: str) -> str:
        path = os.path.join(self.storage_dir, filename)
        with open(path, "w") as f:
            f.write(content)
        return path

    def load(self, file_path: str) -> str:
        with open(file_path, "r") as f:
            return f.read()
