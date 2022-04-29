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
    data = vars.devJdFilePath + 'job_posts.csv'
    # Create a spreadsheet from the Harvard Resume template verbs to
    # use on your resume.
    # filename = 'resumeTemplate.pdf'
    # pageNumber = 3
    # extracted = utils.pdfParser(filename, pageNumber)
    # utils.harvardKeyworder(extracted)

    # Vectorize the data
    # utils.countVectorize()

    # Feature creation
    # utils.featureTextLength(data)
    # utils.makeHist(data)
    text = utils.txtParser(vars.devJdFilePath + 'am6a.txt')
    sent = text.split('.')
    print(sent)


if __name__ == '__main__':
    main()
