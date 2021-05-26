# Following code adapted from Udacity Large Codebases with Libraries course

from typing import List
import pandas

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel

class CSVIngestor(IngestorInterface):
    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
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
