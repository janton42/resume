# Resumationator
#
# Copyright (C) 22022 Jeff Stock
# Author: Jeff Stock <jantonstock@gmail.com>
# For license information, see LICENSE.TXT

"""
DOCSTRING
"""

devFilesPath = './dev/'

devJdFilePath = devFilesPath + 'jds/'

pos_tags = {
    'VERB': ['VB','VBG','VBD', 'VBN','VBN-HL','VERB'],
    'ADJ': ['JJ','JJ-T','ADJ'],
    'NOUN': ['NOUN','NN']
    }


pm_jd_filenames = [
    'prog_man_learn_sys_github_clean.txt',
    'prog_man_plus_clean.txt',
    'prog_man_tradedesk_clean.txt',
    'prog_man_whatsapp_clean.txt',
    'prog_man_prod_ops_chainlinklabs_clean.txt',
    'prog_man_content_prod_coursera.txt',
    'prog_man_mem_cust_insights_linkedin_clean.txt',
    'prog_man_operations_tech_stripe_clean.txt',
    'localization_prog_man_meta_clean.txt'
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

ling_jd_filenames = [
    'linguist_advertiser_safety_google_clean.txt'
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
    'anal_insights_man_clean.txt',
    'cust_anal_man_nextdoor_clean.txt',
    'data_anal_man_bailielumber_clean.txt',
    'people_anal_man_pwc_clean.txt',
    'strat_insights_anal_man_newtonx_clean.txt',
    'prog_man_prod_ops_chainlinklabs_clean.txt',
    'prog_man_content_prod_coursera.txt',
    'prog_man_mem_cust_insights_linkedin_clean.txt',
    'prog_man_operations_tech_stripe_clean.txt',
    'linguist_advertiser_safety_google_clean.txt',
    'localization_prog_man_meta_clean.txt',
    'python_dev_tektalent_clean.txt'
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
    'program',
    'Program',
    'position',
    'manager',
    'Manager',
    'experi',
    'manag',
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
    ]
