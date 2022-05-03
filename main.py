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

    # create a chart of the top 20 most used verbs, adjectives, and
    # nouns

    # jd_parse_filenames = vars.all_jd_filenames
    # jd_set = [utils.txtParser(vars.devJdFilePath + filename) for filename in jd_parse_filenames]
    # utils.chartTokenFreq(jd_set)

    action_words_filepath = vars.devFilesPath + 'action_types.csv'
    harvard_action_tokens_df = utils.actionTokenGetter(action_words_filepath)
    print(harvard_action_tokens_df)

    resume_bullets_filepath = vars.devFilesPath + 'user_input.csv'
    resume_bullets_df = utils.csv_to_df(resume_bullets_filepath)
    resume_bullets_df['verb_stems'] = [list(utils.posFinder(bullet, 'VERB').values()) for bullet in resume_bullets_df['Bullet']]
    # resume_bullet_vstems = [d for d in resume_bullet_vstems if len(list(d)) != 0]

    print(resume_bullets_df)


    matches = {}


    # tokens = utils.tokenCompiler(vars.pm_jd_filenames, 'VERB')
    # print(tokens[4])

if __name__ == '__main__':
    main()
