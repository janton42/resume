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
    am4 = 'am4a.txt'
    am5 = 'am5a.txt'
    am6 = 'am6a.txt'
    opsNoFit1 = 'opsNotit1a.txt'

    am4verbs = utils.verbFinder(am4)
    am5verbs = utils.verbFinder(am5)
    am6verbs = utils.verbFinder(am6)
    opsNoFit1verbs = utils.verbFinder(opsNoFit1)

    print('{}:\n{}'.format('Analytics 4', am4verbs))
    print('{}:\n{}'.format('Analytics 5', am5verbs))
    print('{}:\n{}'.format('Analytics 6', am6verbs))
    print('{}:\n{}'.format('Operations (No Fit)', opsNoFit1verbs))
if __name__ == '__main__':
    main()
