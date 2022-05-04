# Resumationator helps tailor your resume to job posts.
#
# Copyright (C) 2022 Jeff Stock <jantonstock@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>

"""
DOCSTRING
"""
import vars
import os
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
# from nltk.corpus import brown, WordNet

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

def actionTokenGetter(filename):
    csv_in = pd.read_csv(filename)
    working = pd.DataFrame(csv_in)
    ps = nltk.PorterStemmer()
    working['stems'] = [ps.stem(x.lower()) for x in working['action']]
    return working

# takes in a .csv file and returns a pandas data frame object.
def csv_to_df(filename):
    csv_in = pd.read_csv(filename)
    working = pd.DataFrame(csv_in)

    return working

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

def posFinder(text, pos):
    ps = nltk.PorterStemmer()
    tag_set = vars.pos_tags
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
        if stem not in vars.nonsense and len(stem) > 1:
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

def tokenCompiler(jd_set, pos):
    all_tokens = {}
    count = 0
    for jd in jd_set:
        tokens = posFinder(jd, pos)
        for t in tokens:
            all_tokens[count] = tokens[t]
            count += 1
    return all_tokens

def chartPrepper(jd_set, pos):
    all_tokens = tokenCompiler(jd_set, pos)
    fit_tokens = nonsenseFilter(all_tokens)
    common_tokens= freqRanker(fit_tokens)
    ranked = dataGrouper(common_tokens)
    return ranked

# takes in a list of job descriptions
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

    fig, (ax1, ax2, ax3) = plt.subplots(1,3, figsize=(15,10))
    fig.suptitle('Most Common Stems [top 20]')
    ax1.barh(verb_group_names, verb_group_data)
    ax1.set_ylabel('Stems')
    ax1.set_xlabel('Frequency')
    ax1.set_title('Verbs')

    ax2.barh(adj_group_names, adj_group_data)
    ax2.set_xlabel('Frequency')
    ax2.set_title('Adjectives')

    ax3.barh(noun_group_names, noun_group_data)
    ax3.set_xlabel('Frequency')
    ax3.set_title('Nouns')
    plt.show()

def bullet_strength_calculator(res_stem_list, jd_stem_list):
    count = 0
    for stem in res_stem_list:
        if stem in jd_stem_list:
            count += 1
    return count

# def getSynonyms(token_set):
#     synonyms = []
#     for token in token_set:
#         for syn in WordNet.synsets([token]):
#             sunonmys.appen(syn)
#     return synonyms
