"""
Part of the Quote Engine to parse CSV input data files.

The code is adapted from Udacity Large Codebases with Libraries course
"""

from typing import List
import pandas

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class CSVIngestor(IngestorInterface):
    """
    Parse a CSV and return a list of QuoteModel.

    Inherit from IngestorInterface abstract class
    """

    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Parse CSVs to QuoteModels.

        Expects the following quote format in the document:
        quote body - author

        Function class - overrides the default
        1) Check if the extenstion is a CSV and can be managed
        by this class
        2) Use panda to read the CSV and iterate over each row
        to create the QuoteModel for each of them
        """
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        quote_list = []
        df = pandas.read_csv(path, header=0)

        for index, row in df.iterrows():
            new_cat = QuoteModel(row['body'], row['author'])
            quote_list.append(new_cat)

        for quote in quote_list:
            print(f'this is my CSV quote: {quote.body} - {quote.author}')
        return quote_list
