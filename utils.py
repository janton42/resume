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
    fit_tokens = collections.defaultdict(int)

    for d in token_dict:
        for i in token_dict[d]:
            stem = token_dict[d][i]
            if stem not in vars.nonsense:
                fit_tokens[stem] += 1
    return fit_tokens

def chartTokenFreq():

    all_verbs = collections.defaultdict(int)
    all_adj = collections.defaultdict(int)
    all_nouns = collections.defaultdict(int)

    for jd in vars.pm_jd_filenames:
        all_verbs.update(verbs = posFinder(jd, 'VERB'))
        all_adj.update(adjs = posFinder(jd, 'ADJ'))
        all_nouns.update(nouns = posFinder(jd, 'NOUN'))

    fit_verbs = nonsenseFilter(all_verbs)
    fit_adj = nonsenseFilter(all_adj)
    fit_nouns = nonsenseFilter(all_nouns)

    verb_freq_distro = nltk.FreqDist(fit_verbs)
    common_verbs = verb_freq_distro.most_common(10)

    adj_freq_distro = nltk.FreqDist(fit_adj)
    common_adj = adj_freq_distro.most_common(20)

    noun_freq_distro = nltk.FreqDist(fit_nouns)
    common_noun = noun_freq_distro.most_common(20)

    verb_group_data = []
    verb_group_names = []
    common_verbs_dict = collections.defaultdict(list)
    for word in common_verbs:
        verb_group_data.append(word[1])
        verb_group_names.append(word[0])

    adj_group_data = []
    adj_group_names = []
    common_adj_dict = collections.defaultdict(list)
    for word in common_adj:
        adj_group_data.append(word[1])
        adj_group_names.append(word[0])

    noun_group_data = []
    noun_group_names = []
    common_noun_dict = collections.defaultdict(list)
    for word in common_noun:
        noun_group_data.append(word[1])
        noun_group_names.append(word[0])

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
