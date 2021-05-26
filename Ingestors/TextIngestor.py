from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from typing import List


class TextIngestor(IngestorInterface):
    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        quote_list = []
        with open(path, 'r') as f:
            contents = f.read()
            quotes = contents.split('\n')
            for quote in quotes:
                try:
                    quote_text = quote.split(' - ')[0].strip('"')
                    quote_author = quote.split(' - ')[1]
                    quote_list.append(QuoteModel(quote_text, quote_author)) 
                except:
                    print('The string is not structred: body of the quote - author')
                    pass
        for quote in quote_list:
             print(f'this is my TXT quote: {quote.body} - {quote.author}, it comes form: {path}')
        return quote_list
        
        

