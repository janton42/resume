# Resumationator
#
# Copyright (C) 22022 Jeff Stock
# Author: Jeff Stock <jantonstock@gmail.com>
# For license information, see LICENSE.TXT

"""
DOCSTRING
"""

from PyPDF2 import PdfFileReader
import vars as v
import nltk

def pdfParser(filename, pageNumber):
        filePath = v.devFilesPath + filename
        with open(filePath,'rb') as file:
            reader = PdfFileReader(file)
            contents = reader.getPage(pageNumber).extractText().split('\n')
            print(contents)
            return contents
