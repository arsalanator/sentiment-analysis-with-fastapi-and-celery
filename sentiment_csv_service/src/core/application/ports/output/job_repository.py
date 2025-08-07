from abc import ABC, abstractmethod
from typing import Optional


class JobStatus(str):
    PENDING = "PENDING"
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"


class JobRepository(ABC):
    @abstractmethod
    def create_job(self, file_id: str) -> str:
        """Create a new job and return the job ID."""
        pass

    @abstractmethod
    def update_status(self, job_id: str, status: JobStatus) -> None:
        """Update the status of a job."""
        pass

    @abstractmethod
    def get_status(self, job_id: str) -> Optional[JobStatus]:
        """Get the current status of a job."""
        pass
