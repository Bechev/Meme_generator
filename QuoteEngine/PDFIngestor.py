"""
Part of the Quote Engine to parse PDF input data files.

The code is adapted from Udacity Large Codebases with Libraries course
"""

from typing import List
import os
import shutil
import subprocess

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from .TextIngestor import TextIngestor


class PDFIngestor(IngestorInterface):
    """
    Parse a CSV and return a list of QuoteModel.

    Inherit from IngestorInterface abstract class
    """

    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Parse CSVs to QuoteModels.

        Expects the following quote format in the document:
        quote body - author

        Function class - overrides the default
        1) Check if the extenstion is a CSV and can be managed
        by this class
        2) Create a temp directory and copy the pdf file in it
        3) Use a subprocess to transform the pdf in a text file
        4) Feed the text file to the TextIngestor and get back a
        list of QuoteModel
        """
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        quote_list = []
        file_name = path.split('/')[-1]
        folder_path = ''.join(path.rsplit(file_name))
        temp_path = folder_path + 'temp'
        file_temp_path = str(temp_path) + '/' + file_name
        try:
            os.mkdir(temp_path)
        except Exception as e:
            pass

        shutil.copyfile(path, file_temp_path)
        subprocess.run(['pdftotext', file_temp_path])
        txt_file_path = temp_path + '/' + file_name.split('.')[0] + '.txt'
        quote_list = TextIngestor.parse(txt_file_path)
        shutil.rmtree(temp_path)

        return quote_list
