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


import collections
import nltk
import time
import vars

import matplotlib.pyplot as plt
import pandas as pd



def fetch_base_data(filepath):
    data = pd.read_csv(filepath, header=None)
    data.columns = ['label', 'body_text']
    # data['body_text_nostop'] = data['body_text'].apply(lambda x: clean_data(x.lower()))
    return data

def feature_text_length(filepath):
    data = fetch_base_data(filepath)
    data['body_len'] = data['body_text'].apply(lambda x: len(x) - x.count(' '))
    return data

def make_hist(filepath):
    data = feature_text_length(filepath)
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

def pos_finder(text, pos):
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

def nonsense_filter(token_dict):
    fit_tokens = {}
    count = 0
    for d in token_dict:
        stem = token_dict[d]
        if stem not in vars.nonsense and len(stem) > 1:
            fit_tokens[count] = stem
            count += 1
    return fit_tokens

def data_grouper(token_set):
    group_data = []
    group_names = []
    for word in token_set:
        group_data.append(word[1])
        group_names.append(word[0])
        return (group_data, group_names)

def freq_ranker(token_set):
    counter = collections.defaultdict(int)
    for token in token_set:
        counter[token_set[token]] += 1
    ranked = sorted(counter.items(), key=lambda item: item[1],reverse=True)
    return ranked[:20]

def token_compiler(jd_set, pos):
    all_tokens = {}
    count = 0
    for jd in jd_set:
        tokens = pos_finder(jd, pos)
        for t in tokens:
            all_tokens[count] = tokens[t]
            count += 1
    return all_tokens

def chart_prepper(jd_set, pos):
    all_tokens = token_compiler(jd_set, pos)
    fit_tokens = nonsense_filter(all_tokens)
    common_tokens= freq_ranker(fit_tokens)
    ranked = data_grouper(common_tokens)
    return ranked


# takes in a list of job descriptions
def chart_token_freq(jd_set):

    # print('Parsing verb stems...')
    # time.sleep(2)
    verbs = chart_prepper(jd_set, 'VERB')
    verb_group_data = verbs[0]
    verb_group_names = verbs[1]

    # print('Parsing adjective stems...')
    # time.sleep(2.0009)
    adj = chart_prepper(jd_set, 'ADJ')
    adj_group_data = adj[0]
    adj_group_names = adj[1]

    # print('Parsing noun stems...')
    # time.sleep(2.0009)
    nouns = chart_prepper(jd_set, 'NOUN')
    noun_group_data = nouns[0]
    noun_group_names = nouns[1]

    # print('Finding the most impactful language...')
    # time.sleep(2.3)
    # print('Preparing vizualization...')
    # time.sleep(3.4)

    fig, (ax1, ax2, ax3) = plt.subplots(1,3, figsize=(10,10))
    fig.suptitle('Most Common Stems [top 20]')
    ax1.barh(verb_group_names, verb_group_data)
    ax1.invert_yaxis()
    ax1.set_ylabel('Stems')
    ax1.set_xlabel('Frequency')
    ax1.set_title('Verbs')

    ax2.barh(adj_group_names, adj_group_data)
    ax2.invert_yaxis()
    ax2.set_xlabel('Frequency')
    ax2.set_title('Adjectives')

    ax3.barh(noun_group_names, noun_group_data)
    ax3.invert_yaxis()
    ax3.set_xlabel('Frequency')
    ax3.set_title('Nouns')
    plt.show()
