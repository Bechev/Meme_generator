"""
Web portion of the meme generator.

Handles Web requests for the meme generator using Flask and requests
"""

import random
import os
import requests
from flask import Flask, render_template, abort, request
from PIL import Image
from requests.models import parse_header_links

# @TODO Import your Ingestor and MemeEngine classes
from MemeGenerator import MemeEngine
from QuoteEngine import Ingestor

app = Flask(__name__)

meme = MemeEngine('./static')


def setup():
    """Load all resources."""
    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    # TODO: Use the Ingestor class to parse all files in the
    # quote_files variable
    quotes = []
    for quote_file in quote_files:
        parsed_quotes = Ingestor.parse(quote_file)
        for quote in parsed_quotes:
            quotes.append(quote)

    images_path = "./_data/photos/dog/"

    # TODO: Use the pythons standard library os class to find all
    # images within the images images_path directory
    imgs = None
    imgs = []
    for root, dirs, files in os.walk(images_path):
        imgs = [os.path.join(root, name)
                for name in files if name != '.DS_Store']

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """Generate a random meme."""
    # @TODO:
    # Use the random python standard library class to:
    # 1. select a random image from imgs array
    # 2. select a random quote from the quotes array
    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """User input for meme information."""
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """Create a user defined meme."""
    # @TODO:
    # 1. Use requests to save the image from the image_url
    #    form param to a temp local file.
    image_url = request.form['image_url']
    response = requests.get(image_url, allow_redirects=True)
    img = f'./static/{random.randint(0, 100000000)}.png'
    open(img, 'wb').write(response.content)
    # img.close()
    # 2. Use the meme object to generate a meme using this temp
    #    file and the body and author form paramaters.
    body = request.form['body']
    author = request.form['author']
    meme = MemeEngine('./static')
    path = '.' + meme.make_meme(img, body, author)
    # 3. Remove the temporary saved image.
    os.remove(img)

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
