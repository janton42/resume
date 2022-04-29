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
import nltk

from nltk.corpus import brown



def main():
    # import a list of tagged sentences from the Brown corpus
    # this will be used to train the tagger
    brown_tagged_sents = brown.tagged_sents(categories='news')
    brown_sents = brown.sents(categories='news')
    # separate training sets from a test set to test effectiveness of
    # tagger
    size = int(len(brown_tagged_sents) * 0.9)
    train_sents = brown_tagged_sents[:size]
    test_sents = brown_tagged_sents[size:]
    # combine taggers using a BACKOFF TAGGING
    t0 = nltk.DefaultTagger('NN')
    t1 = nltk.UnigramTagger(train_sents, backoff=t0)
    t2 = nltk.BigramTagger(train_sents, backoff=t1)
    t3 = nltk.TrigramTagger(train_sents, backoff=t2)
    print(t3.accuracy(test_sents))

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
    sentences = text.split('.')


if __name__ == '__main__':
    main()
