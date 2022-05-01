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
import nltk
import collections

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from PyPDF2 import PdfFileReader
from nltk.tokenize import WhitespaceTokenizer
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

# removes the words from the Harvard resume
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
    output = {}
    for sentence in text:
        tokens = nltk.word_tokenize(sentence)
        tagged = nltk.pos_tag(tokens,tagset='universal')
        output.update(tagged)
    return output

def posFinder(filename, pos):
    ps = nltk.PorterStemmer()
    tag_set = vars.pos_tags
    text = txtParser(vars.devJdFilePath + filename)
    sentences = text.split('.')
    tagged_sents = tagger(sentences)
    stemmed_tokens = {}
    count = 0
    for token in tagged_sents:
        tag = tagged_sents[token]
        if tag in tag_set[pos]:
            count += 1
            stemmed_tokens[count] = ps.stem(token)

    return stemmed_tokens

def nonsenseFilter(token_dict):
    fit_tokens = {}
    count = 0
    for d in token_dict:
        stem = token_dict[d]
        if stem not in vars.nonsense:
            fit_tokens[count] = stem
            count += 1
    return fit_tokens

def dataGrouper(token_set):
    group_data = []
    group_names = []
    for word in token_set:
        group_data.append(word[1])
        group_names.append(word[0])
    return (group_data, group_names)

def freqRanker(token_set):
    counter = collections.defaultdict(int)
    for token in token_set:
        counter[token_set[token]] += 1
    ranked = sorted(counter.items(), key=lambda item: item[1],reverse=True)
    return ranked[:20]

def chartPrepper(jd_set, pos):
    all_tokens = {}
    count = 0
    for jd in jd_set:
        tokens = posFinder(jd, pos)
        for t in tokens:
            all_tokens[count] = tokens[t]
            count += 1
    fit_tokens = nonsenseFilter(all_tokens)
    common_tokens= freqRanker(fit_tokens)
    return dataGrouper(common_tokens)

def chartTokenFreq(jd_set):

    verbs = chartPrepper(jd_set, 'VERB')
    verb_group_data = verbs[0]
    verb_group_names = verbs[1]

    adj = chartPrepper(jd_set, 'ADJ')
    adj_group_data = adj[0]
    adj_group_names = adj[1]

    nouns = chartPrepper(jd_set, 'NOUN')
    noun_group_data = nouns[0]
    noun_group_names = nouns[1]

    fig, (ax1, ax2, ax3) = plt.subplots(1,3)
    ax1.barh(verb_group_names, verb_group_data)
    ax1.set_xlabel('Frequency')
    ax1.set_title('Most Common Verb Stems [top 10]')

    ax2.barh(adj_group_names, adj_group_data)
    ax2.set_xlabel('Frequency')
    ax2.set_title('Most Common Adjectives')

    ax3.barh(noun_group_names, noun_group_data)
    ax3.set_xlabel('Frequency')
    ax3.set_title('Most Common Nouns')
    plt.show()
