"""
Represent quotes within the Quote Engine.

Takes care of handling quotes once parsed.
"""


class QuoteModel():
    """
    Class to represent quotes.

    Quotes have simply a body and an author
    """

    def __init__(self, body, author):
        """
        Initiate the QuoteModel class.

        Has a body and an author
        """
        self.body = body
        self. author = author

    def __repr__(self):
        """
        Make QuoteModel repr readible for a human.

        Overrides default __repr__ function
        """
        return f'"{self.body}" - {self.author}'
