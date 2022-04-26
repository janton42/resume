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
import jdPreprocess

def main():
    # Create a spreadsheet from the Hearvard Resume template verbs to
    # use on your resume.
    # filename = 'resumeTemplate.pdf'
    # pageNumber = 3
    # extracted = utils.pdfParser(filename, pageNumber)
    # utils.harvardKeyworder(extracted)
    jdPreprocess.fetchBaseData()


if __name__ == '__main__':
    main()
