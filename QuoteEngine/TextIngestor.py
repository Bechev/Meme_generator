"""
Part of the Quote Engine to parse txt input data files.

Handles Txt files
"""
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from typing import List


class TextIngestor(IngestorInterface):
    """
    Parse a CSV and return a list of QuoteModel.

    Inherit from IngestorInterface abstract class
    """

    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Parse Txts to QuoteModels.

        Expects the following quote format in the document:
        quote body - author

        Function class - overrides the default
        1) Check if the extenstion is a .txt and can be managed
        by this class
        2) Open the file and iterate over each paragraph of the
        document to parse the quote
        3) Return a List of QuoteModel
        4) Handle exception if the line is empty and considered
        as a paragraph
        """
        quote_list = []
        with open(path, 'r') as f:
            contents = f.read()
            quotes = contents.split('\n')
            for quote in quotes:
                try:
                    quote_text = quote.split(' - ')[0].strip('"')
                    quote_author = quote.split(' - ')[1]
                    quote_list.append(QuoteModel(quote_text, quote_author))
                except Exception:
                    pass
        return quote_list
