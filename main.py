# Resumationator
#
# Copyright (C) 22022 Jeff Stock
# Author: Jeff Stock <jantonstock@gmail.com>
# For license information, see LICENSE.TXT

"""
DOCSTRING
"""
import utils
import vars

def main():
    fileType = input('Please enter a File Type: ')
    if fileType in vars.pdfTypes:
        filename = input('Please enter a file name: ')
        pageNumber = input('Please enter a page number: ')
        pageNumber = int(pageNumber) - 1
        utils.pdfParser(filename, pageNumber)
    elif fileType in vars.txtTypes:
        filename = input('Please enter a file name: ')
        utils.txtParser(filename)
    elif fileType in vars.keyWords:
        filename = input('Please enter a file name: ')
        pageNumber = input('Please enter a page number: ')
        pageNumber = int(pageNumber) - 1
        extracted = utils.pdfParser(filename, pageNumber)
        utils.harvardKeyworder(extracted)

    else:
        print('Enter a valid file type (currently .pdf and txt are supported)')
        main()

if __name__ == '__main__':
    main()
