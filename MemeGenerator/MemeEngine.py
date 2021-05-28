"""
Create meme.

Resize the image to standard and include
quote provided by the QuoteEngine
"""

from PIL import Image, ImageDraw, ImageFont
import os


class MemeEngine():
    """
    Class to create meme.

    Given an image and a quote, will resize the image and add
    the quote
    """

    def __init__(self, output_dir):
        """
        Initiate an instance of the class.
        
        Arg: output_dir: folder where created meme will be dropped
        """
        self.output_dir = output_dir

    def make_meme(self, img_path, text, author, width=500) -> str:
        """
        Create meme.

        Take an image, open it, extract its name to build output path
        Add text and author, save it and return its path
        Args:
        img_path: input image
        text: body of the quote
        author: author of the quote
        width: max width the output image (meme) will have
        """
        print(f'//////// my image: {img_path}////////////')
        img = Image.open(img_path)
        img_name = img_path.split('/')[-1]
        font = ImageFont.truetype('./_data/Font/LilitaOne-Regular.ttf', 36)
        if width is not None:
            ratio = width/float(img.size[0])
            height = int(ratio*float(img.size[1]))
            img = img.resize((width, height), Image.NEAREST)

        if text is not None:
            draw = ImageDraw.Draw(img)
            draw.text((10, img.height - 100), text, fill='white', font=font)

        if author is not None:
            draw = ImageDraw.Draw(img)
            draw.text((10, img.height - 50), author, fill='white', font=font)

        output_path = self.create_output_path(img_name)
        img.save(output_path)
        return output_path

    def create_output_path(self, img_name):
        """
        Create output file path.

        Handle the creation of the meme output path.
        Takes the image and rename it "meme_"image
        """
        try:
            os.mkdir(self.output_dir)
        except Exception as e:
            print(e)
            pass

        return self.output_dir + '/meme_' + img_name
