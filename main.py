# Resumationator
#
# Copyright (C) 22022 Jeff Stock
# Author: Jeff Stock <jantonstock@gmail.com>
# For license information, see LICENSE.TXT

"""
DOCSTRING
"""
from PyPDF2 import PdfFileReader
import nltk


def main():
    with open('./static/resumeTemplate.pdf','rb') as file:
        reader = PdfFileReader(file)
        print(reader.numPages)
        contents = reader.getPage(3).extractText().split('\n')
        print(contents)
        pass

if __name__ == '__main__':
    main()
