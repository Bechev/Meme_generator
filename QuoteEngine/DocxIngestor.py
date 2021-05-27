"""
Part of the Quote Engine to parse Docx input data files.

The code is adapted from Udacity Large Codebases with Libraries course
"""

from typing import List
import docx

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class DocxIngestor(IngestorInterface):
    """
    Parse a Docx and return a list of QuoteModel.

    Inherit from IngestorInterface abstract class
    """

    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Parse Docx to QuoteModels.

        Expects the following quote format in the document:
        quote body - author

        Function class - overrides the default
        1) Check if the extenstion is a .docx and can be managed
        by this class
        2) Open the file and iterate over each paragraph of the
        document to parse the quote
        3) Return a List of QuoteModel
        """
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        quote_list = []
        doc = docx.Document(path)

        for quote in doc.paragraphs:
            if quote.text != "":
                quote = quote.text.split(' - ')
                quote[0] = quote[0].strip('"')
                quote_list.append(QuoteModel(quote[0], quote[1]))
        return quote_list
