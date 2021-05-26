# Following code adapted from Udacity Large Codebases with Libraries course

from typing import List
import docx

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class DocxIngestor(IngestorInterface):
    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
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
