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
