"""
CLI portion of the meme generator.

Handles CLI requests for the meme generator with 3 arguments
path to image
quote
author
"""

import os
import random
import argparse

from QuoteEngine import Ingestor
from QuoteEngine import QuoteModel
from MemeGenerator import MemeEngine


def generate_meme(path=None, body=None, author=None):
    """Generate a meme given an path and a quote."""
    img = None
    quote = None

    if path is None:
        images = "./_data/photos/dog/"
        imgs = []
        for root, dirs, files in os.walk(images):
            print(root)
            imgs = [os.path.join(root, name)
                    for name in files if name != '.DS_Store']
        img = random.choice(imgs)
    else:
        img = path

    if body is None:
        quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                       './_data/DogQuotes/DogQuotesDOCX.docx',
                       './_data/DogQuotes/DogQuotesPDF.pdf',
                       './_data/DogQuotes/DogQuotesCSV.csv']
        quotes = []
        for f in quote_files:
            quotes.extend(Ingestor.parse(f))

        quote = random.choice(quotes)
    else:
        if author is None:
            raise Exception('Author Required if Body is Used')
        quote = QuoteModel(body, author)
    meme = MemeEngine('./tmp')
    path = meme.make_meme(img, quote.body, quote.author)
    return path


if __name__ == "__main__":

    # @TODO Use ArgumentParser to parse the following CLI arguments
    # path - path to an image file
    # body - quote body to add to the image
    # author - quote author to add to the image
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", help="path to an image file")
    parser.add_argument("--body", help="quote body to add to the image")
    parser.add_argument("--author", help="quote author to add to the image")
    args = parser.parse_args()
    # print(generate_meme(None, None, None))
    # print(args.body)
    print(generate_meme(args.path, args.body, args.author))
