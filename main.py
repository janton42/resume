# Resumationator
#
# Copyright (C) 22022 Jeff Stock
# Author: Jeff Stock <jantonstock@gmail.com>
# For license information, see LICENSE.TXT

"""
DOCSTRING
"""
from utils import pdfParser
from vars import pdfTypes



def main():
    fileType = input('Please enter a File Type: ')
    if fileType in pdfTypes:
        filename = input('Please enter a file name: ')
        pageNumber = input('Please enter a page number: ')
        pageNumber = int(pageNumber) - 1
        pdfParser(filename, pageNumber)

if __name__ == '__main__':
    main()
