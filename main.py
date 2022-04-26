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
    filename = 'resumeTemplate.pdf'
    pageNumber = 3
    extracted = utils.pdfParser(filename, pageNumber)
    utils.harvardKeyworder(extracted)

if __name__ == '__main__':
    main()
