# Following code adapted from Udacity Large Codebases with Libraries course

from abc import ABC, abstractmethod
from typing import List
from .QuoteModel import QuoteModel

class IngestorInterface(ABC):
    allowed_extensions = [QuoteModel]

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        ext = path.split('.')[-1] 
        return ext in cls.allowed_extensions
    
    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List:
        pass