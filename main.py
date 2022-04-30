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
import collections
import nltk

import matplotlib.pyplot as plt

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


    fit_verbs = collections.defaultdict(int)
    all_verbs = collections.defaultdict(int)
    all_adj = collections.defaultdict(int)

    for jd in vars.intel_analyst_filenames:
        all_verbs.update(verbs = utils.verbFinder(jd))
        all_adj.update(adjs = utils.adjFinder(jd))

    for d in all_verbs:
        for i in all_verbs[d]:
            stem = all_verbs[d][i]
            if stem not in vars.nonsense:
                fit_verbs[stem] += 1

    verb_freq_distro = nltk.FreqDist(fit_verbs)
    common_verbs = verb_freq_distro.most_common(10)
    # frequent = {(stem, fit_verbs[stem]) for stem in fit_verbs if fit_verbs[stem] > 1}
    # sorted_frequent_verbs = sorted(frequent, key=lambda word: word[1], reverse=True)

    verb_group_data = []
    verb_group_names = []
    common_verbs_dict = collections.defaultdict(list)
    for word in common_verbs:
        verb_group_data.append(word[1])
        verb_group_names.append(word[0])

    # print(common_verbs_dict)

    # verb_group_data = list(common_verbs.values())
    # verb_group_names = list(common_verbs.keys())

    fig, ax = plt.subplots()
    ax.barh(verb_group_names, verb_group_data)
    ax.set_ylabel('Stems')
    ax.set_xlabel('Frequency')
    ax.set_title('Most Common Verb Stems')
    plt.show()


    # opsNofit_verbs1verbs = utils.verbFinder(opsNofit_verbs1)
    #
    # print('{}:\n{}'.format('Analytics 4', am4verbs))
    # print('{}:\n{}'.format('Analytics 5', am5verbs))
    # print('{}:\n{}'.format('Analytics 6', am6verbs))
    # print('{}:\n{}'.format('Operations (No fit_verbs)', opsNofit_verbs1verbs))
if __name__ == '__main__':
    main()
