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
import nltk

eng_stop_words = nltk.corpus.stopwords.words('english')

contextual_stops = [
    'experience',
    'etc',
    'role',
    'candidate',
    'greenlight',
    'preferred',
    'qualifications',
    'weekly',
    'daily',
    'monthly',
    'quarterly',
    'key',
    'work',
    'dollar',
    'uber',
    'next',
    'com',
    'jan',
    'dec',
    'jun',
    '17',
    '15',
    'playstation',
    'new',
    'nextdoor',
    'across',
    'strong'
    ]

def get_stops(stops):
    for w in eng_stop_words:
        stops.append(w)
    return stops

english_and_contextual_stops = get_stops(contextual_stops)



dot = '·'

devFilesPath = './dev/'

dev_bullets = ''

month_ints = {
    'JAN': 1,
    'FEB': 2,
    'MAR': 3,
    'APR': 4,
    'MAY': 5,
    'JUN': 6,
    'JUL': 7,
    'AUG': 8,
    'SEP': 9,
    'OCT': 10,
    'NOV': 11,
    'DEC': 12
}

dev_person = {
    'name': 'Jeff Stock',
    'email': 'JAntonStock@gmail.com',
    'location': 'San Mateo, CA',
    'linkedin': 'linkedin.com/in/stockj',
    'phone': '+1-707-301-8624'
}

devJdFilePath = devFilesPath + 'jds/'

tailored_resumes_filepath = devFilesPath + 'tailored_resumes/'

pos_tags = {
    'VERB': ['VB','VBG','VBD', 'VBN','VBN-HL','VERB'],
    'ADJ': ['JJ','JJ-T','ADJ'],
    'NOUN': ['NOUN','NN']
    }


pm_jd_filenames = [
    './dev/raw_jd/pm_1.txt',
    './dev/raw_jd/pm_2.txt',
    './dev/raw_jd/pm_3.txt',
    './dev/raw_jd/pm_4.txt',
    './dev/raw_jd/pm_5.txt',
    './dev/raw_jd/pm_6.txt',
    './dev/raw_jd/pm_7.txt',
    './dev/raw_jd/pm_8.txt',
    './dev/raw_jd/pm_9.txt',
    './dev/raw_jd/pm_10.txt',
    './dev/raw_jd/pm_11.txt',
    './dev/raw_jd/pm_12.txt',
    './dev/raw_jd/localization_prog_man_meta.txt'

]

ana_man_filenames = [
    # './dev/jds/ana_insights_man_clean.txt',
    # './dev/jds/cust_ana_man_nextdoor_clean.txt',
    # './dev/jds/data_ana_man_bailielumber_clean.txt',
    './dev/jds/people_ana_man_pwc_clean.txt',
    # './dev/jds/strat_insights_ana_man_newtonx_clean.txt'
]

intel_analyst_filenames = [
    './dev/jds/intel_analyst_alliedunited_clean.txt'
]

ling_jd_filenames = [
    './dev/jds/linguist_advertiser_safety_google_clean.txt'
]

python_dev_jd_filenames = [
    'python_dev_tektalent_clean.txt'
]

all_jd_filenames = [
    'intel_analyst_alliedunited_clean.txt',
    'prog_man_learn_sys_github_clean.txt',
    'prog_man_plus_clean.txt',
    'prog_man_tradedesk_clean.txt',
    'prog_man_whatsapp_clean.txt',
    'ana_insights_man_clean.txt',
    'cust_ana_man_nextdoor_clean.txt',
    'data_ana_man_bailielumber_clean.txt',
    'people_ana_man_pwc_clean.txt',
    'strat_insights_ana_man_newtonx_clean.txt',
    'prog_man_prod_ops_chainlinklabs_clean.txt',
    'prog_man_content_prod_coursera.txt',
    'prog_man_mem_cust_insights_linkedin_clean.txt',
    'prog_man_operations_tech_stripe_clean.txt',
    'linguist_advertiser_safety_google_clean.txt',
    'localization_prog_man_meta_clean.txt',
    'python_dev_tektalent_clean.txt'
]

all_raw_jd = [
    './dev/raw_jd/prog_man_mem_cust_insights_linkedin.txt',
    './dev/programManager_1.txt',
    './dev/programManager_2.txt',
    './dev/programManager_3.txt',
    './dev/programManager_4.txt'
    ]

raw_jd_single_path = ['./dev/raw_jd/ana_insights_man_uber.txt']
resume_pdf_single_path = ['./dev/resume.pdf']
resume_text_single_path = ['./dev/resume.txt']

# a word or phrase meant to inform readers (job seekers) of the most
# relevant skills and technologies needed for a role

anchors = [
    'qualified candidates',
    'qualifications',
    'requirements',
    'required'
    'responsibilities',
    'qualifications'

]

nonsense = [
    'work',
    'involv',
    'look',
    'join',
    'achiev',
    'will',
    'is',
    'must',
    'have',
    'demonstr',
    'includ',
    'quarterly',
    'daily',
    'weekly',
    'monthly',
    'full-time',
    'ideal',
    'WhatsApp',
    'position',
    'quarterli',
    'daili',
    'weekli',
    'monthli',
    'full-tim',
    'employe',
    'role',
    'newtonx',
    'are',
    'be',
    'exist',
    'other',
    'would',
    'should',
    'could',
    'll',
    'ttd',
    'candid',
    'year',
    'need',
    'ha',
    'requir',
    'bi-annu',
    'day-to-day',
    'long-term',
    'oper',
    'abil',
    're',
    'can',
    'like',
    '%',
    'etc',
    'meta',
    'stripe',
    'prefer',
    '-',
    ',',
    '\'',
    '_',
    'v',
    '–',
    '’',
    'hire',
    'use',
    'onlin',
    'think',
    'degre',
    'equival'
    ]
