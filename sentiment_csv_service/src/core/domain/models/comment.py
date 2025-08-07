from dataclasses import dataclass
from enum import Enum
from typing import Optional


class Sentiment(str, Enum):
    POSITIVE = "Positive"
    NEGATIVE = "Negative"
    NEUTRAL = "Neutral"


@dataclass
class Comment:
    id: int
    text: str
    sentiment: Optional[Sentiment] = None