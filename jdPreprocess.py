# Resumationator
#
# Copyright (C) 22022 Jeff Stock
# Author: Jeff Stock <jantonstock@gmail.com>
# For license information, see LICENSE.TXT

"""
DOCSTRING
"""

import string
import re
import pandas as pd
import vars


def removePunct(text):
    text_nopunct = ''.join([char for char in text if char not in string.punctuation])
    return text_nopunct

def tokenize(text):
    tokens = re.split('\W+', text)
    return tokens

def fetchBaseData():
    data = pd.read_csv(vars.devJdFilePath + 'job_posts.csv', header=None)
    data.columns = ['label', 'body_text']
    data ['body_text_clean'] = data['body_text'].apply(lambda x: removePunct(x))
    data ['body_text_tokenized'] = data['body_text_clean'].apply(lambda x: tokenize(x.lower()))

    print(data.head())
    return data
