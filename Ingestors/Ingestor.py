"""
Allocate the inputs to the relevant Ingestor.

Can handle 4 types of files: pdf, txt, csv and docx.
"""

# Following code adapted from Udacity Large Codebases with Libraries course

from typing import List  # Allow to annotate the data contained in the list

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from .TextIngestor import TextIngestor
from .DocxIngestor import DocxIngestor
from .CSVIngestor import CSVIngestor
from .PDFIngestor import PDFIngestor


class Ingestor(IngestorInterface):
    """
    Distribute the files to be parsed to the right parser.

    Inherite from abstract class IngestorInterface.
    This class is in charge of dispatching the work among
    the Ingestors
    """

    importers = [TextIngestor, DocxIngestor, CSVIngestor, PDFIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Check for the file being passed if an ingestor can parse it.

        If so, it triggers the parsing
        """
        for importer in cls.importers:
            if importer.can_ingest(path):
                return importer.parse(path)
