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

import utils
import vars
import time
from datetime import date
import regex
import nltk
import matplotlib

from handlers.file_writer import PDF
from handlers.file_parser import txt_parser, csv_to_df

from sklearn.feature_extraction.text import TfidfVectorizer

def main():
    # STEP 1
    # Analyze a job description, and show the highest weighted ngrams
    # so jobseekers can write tailored bullets

    corpus = utils.corpus_prepper('./input/')
    utils.jd_analyzer(corpus)
    #
    # utils.chartTokenFreq(jd_set)

    # resume_txt = utils.txtParser(vars.devFilesPath + 'clean_resume.txt')
    # # workaround for removing non-latin characters
    # decoded_resume_text = resume_txt.encode('latin-1', 'replace').decode('latin-1')
    # create a chart of the top 20 most used verbs, adjectives, and
    # nouns
    # jd_verb_stems = utils.chartTokenFreq(jd_set)
    # print(type(decoded_resume_text))

    # jd_parse_filenames = vars.ling_jd_filenames
    # this is the type of simple corpus that scikit learn can use for count TFIDF
    jd_set = [txt_parser(filename) for filename in corpus]
    # create an ordered list of verbs from job post(s)
    # utils.chartTokenFreq(jd_set)
    jd_verb_stems = utils.chartPrepper(jd_set,'VERB')[1]
    jd_adj_stems = utils.chartPrepper(jd_set,'ADJ')[1]
    jd_noun_stems = utils.chartPrepper(jd_set,'NOUN')[1]

    # get user input from a .csv file and convert into a pandas data frame
    user_input_filepath = './user_input/user_input.csv'
    user_input_df = csv_to_df(user_input_filepath)
    # stem the verbs in user input resume bullet statements
    # print('Calculating your verb strength...')
    # time.sleep(2.0009)
    user_input_df['verb_stems'] = [list(utils.posFinder(bullet, 'VERB').values()) for bullet in user_input_df['Bullet']]
    user_input_df['verb_strength_score'] = [utils.bullet_strength_calculator(stem_list, jd_verb_stems) for stem_list in user_input_df['verb_stems']]

    # # stem the adjectives in user input resume bullet statements
    user_input_df['adj_stems'] = [list(utils.posFinder(bullet, 'ADJ').values()) for bullet in user_input_df['Bullet']]
    user_input_df['adj_strength_score'] = [utils.bullet_strength_calculator(stem_list, jd_adj_stems) for stem_list in user_input_df['adj_stems']]

    # stem the nouns in user input resume bullet statements
    user_input_df['noun_stems'] = [list(utils.posFinder(bullet, 'NOUN').values()) for bullet in user_input_df['Bullet']]
    user_input_df['noun_strength_score'] = [utils.bullet_strength_calculator(stem_list, jd_noun_stems) for stem_list in user_input_df['noun_stems']]
    user_input_df['total_bullet_strength'] = (user_input_df['verb_strength_score'] + user_input_df['adj_strength_score'] + user_input_df['noun_strength_score'])
    bullet_strength_index_df = user_input_df[['Bullet','total_bullet_strength']]
    # closest_roles_df = user_input_df[['Organization','Title','total_bullet_strength','iso_start_date','iso_end_date']]
    # is_valuable = user_input_df['total_bullet_strength'] > 0
    # is_work_exp = user_input_df['Type'] == 'Work'
    # work_exp =  user_input_df[is_work_exp]
    # valuable_experience = work_exp[is_valuable]
    # value_exp_sorted = valuable_experience.sort_values(by=['iso_start_date','total_bullet_strength'], ascending=False)
    # find current roles
    # is_current = user_input_df['iso_end_date'] == 'None'
    # current_roles = work_exp[is_current]


    pdf = PDF()
    pdf.alias_nb_pages()
    pdf.add_page()
    # Add work experience section
    pdf.add_resume_section('Work', user_input_df)
    # Add leadership and activities section
    pdf.add_resume_section('Leadership', user_input_df)
    # TODO: Add Education
    pdf.add_resume_section('Education', user_input_df)

    # TODO: Add skills section
    pdf.output('./output/Jeff Stock_resume_DEMO.pdf', 'F')



    # tokens = utils.tokenCompiler(vars.pm_jd_filenames, 'VERB')
    # print(tokens[4])

    #Juandale Pringle Windlebug the III has claimed ownership of this vessel

if __name__ == '__main__':
    main()
