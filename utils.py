# Resumationator
#
# Copyright (C) 22022 Jeff Stock
# Author: Jeff Stock <jantonstock@gmail.com>
# For license information, see LICENSE.TXT

"""
DOCSTRING
"""
import vars
import os
import csv
import string
import re
import pandas as pd
import nltk
import numpy as np

from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from PyPDF2 import PdfFileReader
from nltk.tokenize import WhitespaceTokenizer
from matplotlib import pyplot
from nltk.corpus import brown

# pulls the text out of a pdf
def pdfParser(filename, pageNumber):
        filePath = vars.devFilesPath + filename
        with open(filePath,'rb') as file:
            reader = PdfFileReader(file)
            pdfContents = reader.getPage(pageNumber).extractText()
            return pdfContents
#pulls text from a .txt file
def txtParser(filename):
    with open(filename) as file:
        txtContents = file.read()
        return txtContents

def create_working_dict(fileLocation):
	compiledList = csv.reader(open(fileLocation, mode='r', encoding='utf-8-sig'))

	dictList = {}
	key = 0

	for v in compiledList:
	   dictList[key] = v
	   key += 1

	headers = dictList[0]

	del dictList[0]

	labeled = {}
	labeledCounter = 1

	for i in dictList:
		pair = {}
		x = 0
		while x < len(headers):
			k = headers[x]
			v = dictList[i][x]
			pair[k] = v
			x += 1
		labeled[labeledCounter] = pair
		labeledCounter += 1

	return labeled

def create_csv(generator,filename):
	output = []
	headers = []
	for i in generator:
		for a in generator[i].keys():
			if a not in headers:
				headers.append(a)

	output.append(headers)

	for x in generator:
		ind = []
		for b in generator[x].values():
			ind.append(b)
		output.append(ind)

	output_path =  vars.devFilesPath + filename + '.csv'

	with open(output_path, 'w') as csvFile:
		writer = csv.writer(csvFile)
		writer.writerows(output)

# removes the
def harvardKeyworder(wordlist):
    tk = WhitespaceTokenizer()
    tokens = tk.tokenize(wordlist)
    output = []
    for t in tokens:
        output.append([t])
    output_path = vars.devFilesPath + 'harvard_tokens.csv'
    with open(output_path, 'w') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(output)

# data cleaning
def cleanData(text):
    # gather stopwords from the nltk corpus
    stopword = nltk.corpus.stopwords.words('english')
    # initialize a stemmer
    ps = nltk.PorterStemmer()

    # remove punctuation
    text = ''.join([char for char in text if char not in string.punctuation])
    # tokenize
    tokens = re.split('\W+', text)
    # make a list of stemmed non-stopwords
    # this is for ngram count vectorizing.
    # do not join when using simple count or TFIDF vectorizing
    # text = ' '.join([ps.stem(word) for word in tokens if word not in stopword])
    text = [ps.stem(word) for word in tokens if word not in stopword]
    return text

def fetchBaseData(filepath):
    data = pd.read_csv(filepath, header=None)
    data.columns = ['label', 'body_text']
    # data['body_text_nostop'] = data['body_text'].apply(lambda x: cleanData(x.lower()))
    return data


def countVectorize():
    data = pd.read_csv(vars.devJdFilePath + 'job_posts.csv', header=None)
    data.columns = ['label', 'body_text']
    # this step is needed if using ngram count vectorizing
    # not needed for TFIDF or simple count vectorizing
    # data['cleaned_text'] = data['body_text'].apply(lambda x: cleanData(x))
    # set the number of ngrams from each gram is a token. Multiple
    # ngrams
    # ngramVect = CountVectorizer(2,2)
    tfidfVect = TfidfVectorizer(analyzer=cleanData)
    X_counts = tfidfVect.fit_transform(data['body_text'])
    X_counts_df = pd.DataFrame(X_counts.toarray())
    X_counts_df.columns = tfidfVect.get_feature_names()
    print(X_counts_df)


def featureTextLength(filepath):
    data = fetchBaseData(filepath)
    data['body_len'] = data['body_text'].apply(lambda x: len(x) - x.count(' '))
    return data

def makeHist(filepath):
    data = featureTextLength(filepath)
    bins = np.linspace(2, 6000, 100)
    pyplot.hist(data[data['label'] == 'nofit']['body_len'], bins,alpha=0.5, label='nofit')
    pyplot.hist(data[data['label'] == 'fit']['body_len'], bins,alpha=0.5, label='fit')
    pyplot.legend(loc='upper left')
    pyplot.show()

def tagger(text):
    # import a list of tagged sentences from the Brown corpus
    # this will be used to train the tagger
    # brown_tagged_sents = brown.tagged_sents(categories='news')
    # brown_sents = brown.sents(categories='news')
    # # separate training sets from a test set to test effectiveness of
    # # tagger
    # size = int(len(brown_tagged_sents) * 0.9)
    # train_sents = brown_tagged_sents[:size]
    # test_sents = brown_tagged_sents[size:]
    # # combine taggers using a BACKOFF TAGGING
    # t0 = nltk.DefaultTagger('NN')
    # t1 = nltk.UnigramTagger(train_sents, backoff=t0)
    # t2 = nltk.BigramTagger(train_sents, backoff=t1)
    # TrigramTagger can be added, but does not improve accuracy, so was
    # intentionally ommitted
    output = {}
    for sentence in text:
        tokens = nltk.word_tokenize(sentence)
        # tagged = dict(t2.tag(tokens))
        tagged = nltk.pos_tag(tokens,tagset='universal')
        output.update(tagged)
    return output

def tokenStemmer(tagged_sents):
    ps = nltk.PorterStemmer()
    verbs = {}
    count = 0
    for word in tagged_sents:
        tag = tagged_sents[word]
        if tag in vars.verb_tags:
            count += 1
            verbs[count] = ps.stem(word)
        # else:
        #     print(tag)
    return verbs

def verbFinder(filename):
    text = txtParser(vars.devJdFilePath + filename)
    sentences = text.split('.')
    tagged_sents = tagger(sentences)
    stems = tokenStemmer(tagged_sents)
    return stems

def adjFinder(filename):
    ps = nltk.PorterStemmer()
    text = txtParser(vars.devJdFilePath + filename)
    sentences = text.split('.')
    tagged_sents = tagger(sentences)
    adjs = {}
    count = 0
    for word in tagged_sents:
        tag = tagged_sents[word]
        if tag in vars.adj_tags:
            count += 1
            adjs[count] = ps.stem(word)

    return adjs

def nounFinder(filename):
    ps = nltk.PorterStemmer()
    text = txtParser(vars.devJdFilePath + filename)
    sentences = text.split('.')
    tagged_sents = tagger(sentences)
    nouns = {}
    count = 0
    for word in tagged_sents:
        tag = tagged_sents[word]
        if tag in vars.noun_tags:
            count += 1
            nouns[count] = ps.stem(word)

    return nouns
