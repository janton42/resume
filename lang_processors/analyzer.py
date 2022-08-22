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


import vars
import nltk
import re
import string
import datetime

import pandas as pd
from handlers.file_parser import csv_to_list

from nltk import pos_tag, word_tokenize
from nltk.tokenize import WhitespaceTokenizer
from sklearn.feature_extraction.text import TfidfVectorizer
from vars import english_and_contextual_stops as stop_set

def ngram_weighter(lower_bound, upper_bound, filepath_list):
    '''
    takes a list of file paths, boundaries (upper and lower) for
    the ngram_range parameter of TfidfVectorizer
    returns the top 20 most important ngrams
    lower_bound = integer representing the lower bound of ngram_range
    upper_bound = integer representing the upper bound of ngram_range
    filepath_list = list of filepaths to job post text files

    '''
    vectorizer = TfidfVectorizer(input='filename', ngram_range=(lower_bound,upper_bound), stop_words=stop_set)
    X_tfidf = vectorizer.fit_transform(filepath_list)

    end = X_tfidf.shape[1]
    feature_names = vectorizer.get_feature_names()
    X_tfidf_df = pd.DataFrame(X_tfidf.toarray())
    X_tfidf_df.columns = feature_names
    total = X_tfidf_df.sum()
    total.name = 'Total'

    X_tfidf_df = X_tfidf_df.append(total.transpose())

    X_tfidf_df.sort_values(by='Total', axis=1, inplace=True, ascending=False, na_position='last')
    top_twenty = X_tfidf_df.iloc[:,:20].columns

    return top_twenty


def jd_analyzer(jds):
    n_grams = {
        'unigrams': ngram_weighter(1,1,jds),
        'bigrams': ngram_weighter(2,2,jds),
        'trigrams': ngram_weighter(3,3,jds)
    }
    return n_grams

def bullet_strength_calculator(res_stem_list, jd_stem_list):
    count = 0
    for stem in res_stem_list:
        if stem in jd_stem_list:
            count += 1
    return count

def bullet_length_comparison(bullet):
    high = 75 * 2
    low = 50 * 2

    return 'Good' if len(bullet) < high and len(bullet) > low else 'Bad'

def pos_tagger(sentence: str):
    return pos_tag(word_tokenize(sentence))


def starts_with_VBN(pos_set):
    return True if pos_set[0][1] == 'VBN' else False

def starts_strong(sentence: str) -> bool:
    words = word_tokenize(sentence)
    start = words[0].lower()
    # fetch strong verbs
    strong_verb_path = './user_input/action_verbs.csv'
    strong_verbs_list = csv_to_list(strong_verb_path)
    return start in strong_verbs_list


# # data cleaning
# def clean_data(text):
#     # gather stopwords from the nltk corpus
#     stopword = nltk.corpus.stopwords.words('english')
#     # initialize a stemmer
#     ps = nltk.PorterStemmer()
#     # remove punctuation
#     text = ''.join([char for char in text if char not in string.punctuation])
#     # tokenize
#     tokens = re.split('\W+', text)
#     text = [ps.stem(word) for word in tokens if word not in stopword]
#     return text
#
# def count_vectorize():
#     tfidfVect = TfidfVectorizer(analyzer=clean_data)
#     X_counts = tfidfVect.fit_transform(data['body_text'])
#     X_counts_df = pd.DataFrame(X_counts.toarray())
#     X_counts_df.columns = tfidfVect.get_feature_names()
#     print(X_counts_df)
#
# # removes the words from the Harvard resume
# def harvardKeyworder(wordlist):
#     tk = WhitespaceTokenizer()
#     tokens = tk.tokenize(wordlist)
#     output = []
#     for t in tokens:
#         output.append([t])
#     output_path = vars.devFilesPath + 'harvard_tokens.csv'
#     with open(output_path, 'w') as csvFile:
#         writer = csv.writer(csvFile)
#         writer.writerows(output)
