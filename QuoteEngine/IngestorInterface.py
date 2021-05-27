"""
Interface to manage quote ingestors.

Abstract class to be used accross all ingestors
"""
from abc import ABC, abstractmethod
from typing import List
from .QuoteModel import QuoteModel


class IngestorInterface(ABC):
    """
    Abstract class used accross all ingestors.

    2 classes methods and a list of allowed extensions
    The allowed extensions are defined by each Ingestor
    """

    allowed_extensions = [QuoteModel]

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """
        Validate if a file can be ingested by the Quote Engine.

        Check the extension of the file that needs to be parsed
        by exctracting the string after the last point in the
        path.
        Return True if this string is in the allowed_extensions
        """
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List:
        """
        Parse data and return a QuoteModel list.

        Abstract method overriden by each subclass
        """
        pass
