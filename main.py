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

def main():

    # data = vars.devJdFilePath + 'job_posts.csv'
    # Create a spreadsheet from the Harvard Resume template verbs to
    # use on your resume.
    # filename = 'resumeTemplate.pdf'
    # pageNumber = 3
    # extracted = utils.pdfParser(filename, pageNumber)
    # utils.harvardKeyworder(extracted)



    jd_parse_filenames = vars.all_jd_filenames
    jd_set = [utils.txtParser(vars.devJdFilePath + filename) for filename in jd_parse_filenames]


    # create a chart of the top 20 most used verbs, adjectives, and
    # nouns
    # jd_verb_stems = utils.chartTokenFreq(jd_set)

    # create an ordered list of verbs from job post(s)
    jd_verb_stems = utils.chartPrepper(jd_set,'VERB')[1]
    jd_adj_stems = utils.chartPrepper(jd_set,'ADJ')[1]

    # stems the verb suggestions from the Harvard template
    action_words_filepath = vars.devFilesPath + 'action_types.csv'
    harvard_action_tokens_df = utils.actionTokenGetter(action_words_filepath)
    # print(harvard_action_tokens_df)


    # get user input from a .csv file and convert into a pandas data frame
    user_input_filepath = vars.devFilesPath + 'user_input.csv'
    user_input_df = utils.csv_to_df(user_input_filepath)
    # stem the verbs in user input resume bullet statements
    user_input_df['verb_stems'] = [list(utils.posFinder(bullet, 'VERB').values()) for bullet in user_input_df['Bullet']]

    user_input_df['verb_strength_score'] = [utils.bullet_strength_calculator(stem_list, jd_verb_stems) for stem_list in user_input_df['verb_stems']]




    print(user_input_df.sort_values(by='verb_strength_score', ascending=False))
    #
    # print(jd_verb_stems)




    matches = {}


    # tokens = utils.tokenCompiler(vars.pm_jd_filenames, 'VERB')
    # print(tokens[4])

if __name__ == '__main__':
    main()
