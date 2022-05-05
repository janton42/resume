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
import pandas as pd
import regex

from file_writer import PDF

def main():

    # data = vars.devJdFilePath + 'job_posts.csv'
    # Create a spreadsheet from the Harvard Resume template verbs to
    # use on your resume.
    # filename = 'resumeTemplate.pdf'
    # pageNumber = 3
    # extracted = utils.pdfParser(filename, pageNumber)
    # utils.harvardKeyworder(extracted)



    jd_parse_filenames = vars.pm_jd_filenames
    jd_set = [utils.txtParser(vars.devJdFilePath + filename) for filename in jd_parse_filenames]
    resume_txt = utils.txtParser(vars.devFilesPath + 'clean_resume.txt')
    # workaround for removing non-latin characters
    decoded_resume_text = resume_txt.encode('latin-1', 'replace').decode('latin-1')
    # create a chart of the top 20 most used verbs, adjectives, and
    # nouns
    # jd_verb_stems = utils.chartTokenFreq(jd_set)
    print(type(decoded_resume_text))
    # create an ordered list of verbs from job post(s)
    jd_verb_stems = utils.chartPrepper(jd_set,'VERB')[1]
    jd_adj_stems = utils.chartPrepper(jd_set,'ADJ')[1]
    jd_noun_stems = utils.chartPrepper(jd_set,'NOUN')[1]

    # stems the verb suggestions from the Harvard template
    action_words_filepath = vars.devFilesPath + 'action_types.csv'
    harvard_action_tokens_df = utils.actionTokenGetter(action_words_filepath)
    # print(harvard_action_tokens_df)


    # get user input from a .csv file and convert into a pandas data frame
    user_input_filepath = vars.devFilesPath + 'user_input.csv'
    user_input_df = utils.csv_to_df(user_input_filepath)
    # stem the verbs in user input resume bullet statements
    # print('Calculating your verb strength...')
    # time.sleep(2.0009)
    user_input_df['verb_stems'] = [list(utils.posFinder(bullet, 'VERB').values()) for bullet in user_input_df['Bullet']]
    user_input_df['verb_strength_score'] = [utils.bullet_strength_calculator(stem_list, jd_verb_stems) for stem_list in user_input_df['verb_stems']]

    # stem the adjectives in user input resume bullet statements
    user_input_df['adj_stems'] = [list(utils.posFinder(bullet, 'ADJ').values()) for bullet in user_input_df['Bullet']]
    user_input_df['adj_strength_score'] = [utils.bullet_strength_calculator(stem_list, jd_adj_stems) for stem_list in user_input_df['adj_stems']]

    # stem the nouns in user input resume bullet statements
    user_input_df['noun_stems'] = [list(utils.posFinder(bullet, 'NOUN').values()) for bullet in user_input_df['Bullet']]
    user_input_df['noun_strength_score'] = [utils.bullet_strength_calculator(stem_list, jd_noun_stems) for stem_list in user_input_df['noun_stems']]
    user_input_df['total_bullet_strength'] = (user_input_df['verb_strength_score'] + user_input_df['adj_strength_score'] + user_input_df['noun_strength_score'])
    # bullet_strength_index_df = user_input_df[['Bullet','total_bullet_strength']]
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
    # Add a new resume section
    pdf.add_resume_section('Work', user_input_df)
    pdf.add_resume_section('Leadership', user_input_df)
    # Add a new Organization and its location on the same line, left-
    # and right-aligned, respectively
    # pdf.add_resume_org(org, location)
    # add a Position Title and the start/end dates on the same line,
    # left and right-aligned, respectively
    # pdf.add_role(org, title, user_input_df)
    pdf.output(vars.tailored_resumes_filepath + 'tailored_61.pdf', 'F')



    # tokens = utils.tokenCompiler(vars.pm_jd_filenames, 'VERB')
    # print(tokens[4])

    #Juandale Pringle Windlebug the III has claimed ownership of this vessel
if __name__ == '__main__':
    main()
