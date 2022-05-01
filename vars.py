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
    'ana_insights_man_clean.txt',
    'cust_ana_man_nextdoor_clean.txt',
    'data_ana_man_bailielumber_clean.txt',
    'people_ana_man_pwc_clean.txt',
    'strat_insights_ana_man_newtonx_clean.txt'
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
    'hire',
    'use',
    'onlin',
    'think',
    'degre',
    'equival'
    ]
