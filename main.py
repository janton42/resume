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


    fit = collections.defaultdict(int)
    all_verbs = collections.defaultdict(int)

    for jd in vars.intel_analyst_filenames:
        all_verbs.update(am5verbs = utils.verbFinder(jd))

    for d in all_verbs:
        for i in all_verbs[d]:
            stem = all_verbs[d][i]
            if stem not in vars.nonsense:
                fit[stem] += 1

    freq_distro = nltk.FreqDist(fit)
    common = freq_distro.most_common(10)
    # frequent = {(stem, fit[stem]) for stem in fit if fit[stem] > 1}
    # sorted_frequent_verbs = sorted(frequent, key=lambda word: word[1], reverse=True)

    group_data = []
    group_names = []
    common_dict = collections.defaultdict(list)
    for word in common:
        group_data.append(word[1])
        group_names.append(word[0])

    # print(common_dict)

    # group_data = list(common.values())
    # group_names = list(common.keys())

    fig, ax = plt.subplots()
    ax.barh(group_names, group_data)
    plt.show()
    

    # opsNoFit1verbs = utils.verbFinder(opsNoFit1)
    #
    # print('{}:\n{}'.format('Analytics 4', am4verbs))
    # print('{}:\n{}'.format('Analytics 5', am5verbs))
    # print('{}:\n{}'.format('Analytics 6', am6verbs))
    # print('{}:\n{}'.format('Operations (No Fit)', opsNoFit1verbs))
if __name__ == '__main__':
    main()
