# Resumationator helps tailor your resume to job posts.

# Copyright (C) 2022 Jeff Stock <jantonstock@gmail.com>

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>

from handlers.file_writer import PDF
from handlers.file_parser import txt_parser, csv_to_df, create_working_dict, corpus_prepper
from lang_processors.analyzer import jd_analyzer, bullet_strength_calculator, bullet_length_comparison
from lang_processors.visualizations import chart_token_freq, chart_prepper, pos_finder, token_compiler
from lang_processors.composer import synonymizer, create_text

def main():
    # STEP 1
    # Analyze a job description, and show the highest weighted one, two,
    # and three word combinations,
    # so jobseekers can write tailored bdullets

    # Path to folder containing job descriptions in .txt format
    input_path = './input/'
    output_path = './output/'
    resume_filename = 'Jeff Stock_resume_4.pdf'

    # Create a useable corpus of words for analysis from the input jds.
    corpus = corpus_prepper(input_path)

    # Display key terms in one-, two-, and three-word combinations
    jd_analyzer(corpus)

    # Turn text from JDs into simple corpus that scikit learn uses for
    # count TFIDF
    jd_set = [txt_parser(filename) for filename in corpus]

    # Make a chart showing keywords
    # chart_token_freq(jd_set)

    # create ordered lists of  each part of spech from job post(s)
    jd_verb_stems = chart_prepper(jd_set,'VERB')[1]
    jd_adj_stems = chart_prepper(jd_set,'ADJ')[1]
    jd_noun_stems = chart_prepper(jd_set,'NOUN')[1]

    # get user input from a .csv file and convert into a pandas data frame
    user_input_filepath = './user_input/user_input.csv'
    user_input_df = csv_to_df(user_input_filepath)

    # add lengths of bullets
    user_input_df['bullet_length'] = [bullet_length_comparison(bullet) for bullet in user_input_df['Bullet']]

    # fetch strong verbs
    strong_verb_path = './user_input/action_verbs.csv'
    strong_verbs_dict = create_working_dict(strong_verb_path)
    print(strong_verbs_dict)
    tester = ['restored', 'financed', 'developed','ate']
    for test in tester:
        if test in strong_verbs_dict:
            print(True)
        else:
            print(False)
    # stem the parts of speech in user input resume bullet statements
    # VERBS
    user_input_df['verb_stems'] = [list(pos_finder(bullet, 'VERB').values()) for bullet in user_input_df['Bullet']]
    user_input_df['verb_strength_score'] = [bullet_strength_calculator(stem_list, jd_verb_stems) for stem_list in user_input_df['verb_stems']]

    # ADJ
    user_input_df['adj_stems'] = [list(pos_finder(bullet, 'ADJ').values()) for bullet in user_input_df['Bullet']]
    user_input_df['adj_strength_score'] = [bullet_strength_calculator(stem_list, jd_adj_stems) for stem_list in user_input_df['adj_stems']]

    # NOUNS
    user_input_df['noun_stems'] = [list(pos_finder(bullet, 'NOUN').values()) for bullet in user_input_df['Bullet']]
    user_input_df['noun_strength_score'] = [bullet_strength_calculator(stem_list, jd_noun_stems) for stem_list in user_input_df['noun_stems']]
    user_input_df['total_bullet_strength'] = (user_input_df['verb_strength_score'] + user_input_df['adj_strength_score'] + user_input_df['noun_strength_score'])
    bullet_strength_index_df = user_input_df[['Bullet','total_bullet_strength']]


    # Write the resume to a .pdf file
    option = input('Would you like to create a .pdf (y/n)? ')
    if option == 'y':
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
        pdf.output(output_path + resume_filename, 'F')

        print('Your .pdf has been created.\nGood bye!\n')
    else:
        print("Juandale Pringle Windlebug the III has claimed ownership of this vessel")

        # Juandale Pringle Windlebug the III has claimed ownership of this vessel
if __name__ == '__main__':
    main()
