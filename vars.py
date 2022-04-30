# Resumationator
#
# Copyright (C) 22022 Jeff Stock
# Author: Jeff Stock <jantonstock@gmail.com>
# For license information, see LICENSE.TXT

"""
DOCSTRING
"""

pdfTypes = {'pdf', '.pdf','PDF','.PDF','Portable Document Format','portable document format', 'pdf file'}
txtTypes = {'txt', 'text', '.txt','plain text'}
keyWords = {'Keyword', 'kwords','keywords','keyword','kword','keyWord','KeyWord','keyWords'}

devFilesPath = './dev/'

devJdFilePath = devFilesPath + 'jds/'

# patterns for regular expression tagger
patterns = [
    (r'.*ing$','VBG'),              # gerunds
    (r'.*ed$', 'VBD'),              # simple past
    (r'.*es$','VBZ'),               # 3rd singular present
    (r'.*ould$','MD'),              # modals
    (r'.*\'s$','NN$'),              # possesive nouns (including pronouns)
    (r'.*s$','NNS'),                # plural nouns
    (r'^-?[0-9]+(\.[0-9]+)?$','CD'),# plural nouns
    (r'.*','NN')                    # nouns (default)
]

verb_tags = ['VB','VBG','VBD', 'VBN','VBN-HL','VERB']
adj_tags = ['JJ','JJ-T','ADJ']
noun_tags = ['NOUN','NN']
nonsense = ['work', 'involv','look','join','achiev','will', 'is']

pm_jd_filenames = [
    'prog_man_learn_sys_github_clean.txt',
    'prog_man_plus_clean.txt',
    'prog_man_tradedesk_clean.txt',
    'prog_man_whatsapp_clean.txt'
]

ana_man_filenames = [
    'anal_insights_man_clean.txt',
    'cust_anal_man_nextdoor_clean.txt',
    'data_anal_man_bailielumber_clean.txt',
    'people_anal_man_pwc_clean.txt',
    'strat_insights_anal_man_newtonx_clean.txt'
]

intel_analyst_filenames = [
    'intel_analyst_alliedunited_clean.txt'
]
