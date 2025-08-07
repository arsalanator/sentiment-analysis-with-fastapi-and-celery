from dataclasses import dataclass
from enum import Enum
from typing import Optional


class Sentiment(str, Enum):
    POSITIVE = "Positive"
    NEGATIVE = "Negative"
    NEUTRAL = "Neutral"
    UNKNOWN = "unknown"


@dataclass
class Comment:
    id: str
    text: str
    sentiment: Sentiment = Sentiment.UNKNOWN