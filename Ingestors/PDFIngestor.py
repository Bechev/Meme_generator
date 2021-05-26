# Following code adapted from Udacity Large Codebases with Libraries course

from typing import List
import os
import shutil
import subprocess

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from .TextIngestor import TextIngestor


class PDFIngestor(IngestorInterface):
    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')
        
        quote_list =[]
        file_name =path.split('/')[-1]
        folder_path = ''.join(path.rsplit(file_name))
        temp_path = folder_path + 'temp'
        file_temp_path = str(temp_path) + '/' + file_name
        try:
            os.mkdir(temp_path)
        except:
            pass

        shutil.copyfile(path, file_temp_path)
        subprocess.run(['pdftotext', '-simple', file_temp_path])
        txt_file_path = temp_path + '/' + file_name.split('.')[0] + '.txt'
        quote_list = TextIngestor.parse(txt_file_path)
        shutil.rmtree(temp_path)
    
        return quote_list
