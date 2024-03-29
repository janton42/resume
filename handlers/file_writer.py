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

import os
import vars
import time
from datetime import date
import pandas as pd

from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.person = vars.dev_person_1
        # self.image('./dev/visual/HiredLabs-Icon.png',x=91, y=8, h=7)
        # self.image('./dev/visual/HiredLabs-Icon.png',x=121, y=8, h=7)
        self.set_font('Arial','B', 12)
        self.cell(200, 5, self.person['name'], 'B', 1, 'C')
        self.set_font('Arial',style='',size=10)
        self.cell(200, 5, '{} | {} | {} | {}'.format(
            self.person['email'],
            self.person['location'],
            self.person['linkedin'],
            self.person['phone']
        ), 0, 0, 'C')
        self.ln(10)

    def add_role(self, org, title, user_input_df, section_type):
        is_org = user_input_df['Organization'] == org
        one_org = user_input_df[is_org]
        is_role = one_org['Title'] == title
        role = one_org[is_role]

        if section_type == 'Work':
            is_valuable = role['total_bullet_strength'] > 0
            most_valuable_bullets = role[is_valuable].sort_values(by='total_bullet_strength', ascending=False)
            try:
                start_month = most_valuable_bullets['Start Month'].unique()[0]
            except:
                most_valuable_bullets = role.sort_values(by='total_bullet_strength',ascending=False)
                # print(most_valuable_bullets)

        elif section_type == 'Leadership':
            most_valuable_bullets = role.sort_values(by='total_bullet_strength',ascending=False)

        start_month = most_valuable_bullets['Start Month'].unique()[0]
        start_year = most_valuable_bullets['Start Year'].unique()[0]
        end_month = most_valuable_bullets['End Month'].unique()[0]
        end_year = most_valuable_bullets['End Year'].unique()[0]
        start_date = '{} {}'.format(start_month, start_year)
        end_date = '{} {}'.format(end_month, end_year) if end_month != 'None' and end_year != 'None' else 'Present'

        dates = '{} - {}'.format(start_date,end_date)
        most_valuable_bullets = most_valuable_bullets[:3]
        role_bullets = '\n'.join(most_valuable_bullets['Bullet'])

        self.set_font('Times','B', size=11)
        self.cell(w=100, h=5, txt=title,ln=0,align='L')
        self.set_font('Times', size=11)
        self.cell(w=80, h=5, txt=dates, ln=1, align='R')
        self.ln(1)
        self.cell(w=8, h=5,ln=0)
        self.multi_cell(172, 5, role_bullets, 0, 'L')
        self.ln(h=4)

    def add_course(self, org, title, user_input_df):
        is_org = user_input_df['Organization'] == org
        one_org = user_input_df[is_org]
        is_course = one_org['Title'] == title
        course = one_org[is_course]

        start_month = course['Start Month'].unique()[0]
        start_year = course['Start Year'].unique()[0]
        end_month = course['End Month'].unique()[0]
        end_year = course['End Year'].unique()[0]
        start_date = '{} {}'.format(start_month, start_year)
        end_date = '{} {}'.format(end_month, end_year) if end_month != 'None' and end_year != 'None' else 'Present'
        dates = '{} - {}'.format(start_date,end_date)

        self.set_font('Times','B', size=11)
        self.cell(w=100, h=5, txt=title,ln=0,align='L')
        self.set_font('Times', size=11)
        self.cell(w=80, h=5, txt=dates, ln=1, align='R')
        self.ln(4)

    def add_resume_org(self, org, user_input_df, section_type):
        is_org = user_input_df['Organization'] == org
        one_org = user_input_df[is_org]
        location = one_org['Location'].unique()[0]

        self.set_font('Times','B', size=11)
        self.cell(w=100, h=5, txt=org.upper(),ln=0,align='L')
        self.set_font('Times', size=11)
        self.cell(w=80, h=5, txt=location, ln=1, align='R')
        self.ln(1)
        date_sorted_roles = one_org.sort_values(by=['iso_start_date'], ascending=False)
        unique_roles = date_sorted_roles['Title'].unique()
        for title in unique_roles:
            if section_type == 'Work' or section_type == 'Leadership':
                self.add_role(org, title, user_input_df, section_type)
            elif section_type == 'Education':
                self.add_course(org, title, user_input_df)

    def add_resume_section(self, section_type, user_input_df):
        if section_type == 'Work':
            section_title = 'Experience'
            self.set_font('Times','B', size=11)
            self.cell(w=200, h=5, txt=section_title, ln=1, align='C')
            is_work_exp = user_input_df['Type'] == 'Work'
            work_exp =  user_input_df[is_work_exp]
            date_sorted_orgs = work_exp.sort_values(by=['iso_start_date'], ascending=False)
            unique_orgs = date_sorted_orgs['Organization'].unique()
            for org in unique_orgs:
                self.add_resume_org(org, user_input_df, section_type)
        elif section_type == 'Leadership':
            section_title = 'Leadership & Activities'
            self.set_font('Times','B', size=11)
            self.cell(w=200, h=5, txt=section_title, ln=1, align='C')
            is_leadership_exp = user_input_df['Type'] == 'Leadership'
            leadership_exp = user_input_df[is_leadership_exp]
            date_sorted_orgs = leadership_exp.sort_values(by=['iso_start_date'], ascending=False)
            unique_orgs = date_sorted_orgs['Organization'].unique()
            for org in unique_orgs:
                self.add_resume_org(org, user_input_df, section_type)
        elif section_type == 'Education':
            section_title = 'Education'
            self.set_font('Times','B', size=11)
            self.cell(w=200, h=5, txt=section_title, ln=1, align='C')
            is_edu_exp = user_input_df['Type'] == 'Education'
            edu_exp = user_input_df[is_edu_exp]
            date_sorted_orgs = edu_exp.sort_values(by=['iso_start_date'], ascending=False)
            unique_orgs = date_sorted_orgs['Organization'].unique()
            for org in unique_orgs:
                self.add_resume_org(org, user_input_df, section_type)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')

def write_resume(user_input_df):
    resumes_folder = './output/resumes/'
    # files = os.listdir(path=resumes_folder)
    # if len(files) > 0:
    #     for f in files:
    #         try:
    #             os.remove(resumes_folder + f)
    #         except IsADirectoryError:
    #             print(f + ' is a directory.')
    #             pass
    #         except FileNotFoundError:
    #             print(f + ' not found.')
    #             pass
    resume_filename = input('Enter a resume file name:\n\t')
    pdf = PDF()
    pdf.alias_nb_pages()
    pdf.add_page()

    top = input('Which section should go first, "Education"(1), or "Experience"(2)?')
    leadership = input('Include "Leadership & Activities" section (y/n)?')

    if int(top) == 1:
        # Add Education
        pdf.add_resume_section('Education', user_input_df)
        if leadership == 'y':
            # Add leadership and activities section
            pdf.add_resume_section('Leadership', user_input_df)
        # Add work experience section
        pdf.add_resume_section('Work', user_input_df)

    elif int(top) == 2:
        # Add work experience section
        pdf.add_resume_section('Work', user_input_df)
        if leadership == 'y':
            # Add leadership and activities section
            pdf.add_resume_section('Leadership', user_input_df)
        # Add Education
        pdf.add_resume_section('Education', user_input_df)



    # TODO: Add skills section
    pdf.output(resumes_folder + resume_filename, 'F')

    print('Your .pdf has been created.\nGood bye!\n')
    print("Juandale Pringle Windlebug the III has claimed ownership of this vessel")

    # Juandale Pringle Windlebug the III has claimed ownership of this vessel
def analysis_reporter(analysis,jds,title):
    analysis_folder = './output/analysis_reports/'
    # files = os.listdir(path=analysis_folder)
    # if len(files) > 0:
    #     for f in files:
    #         try:
    #             os.remove(analysis_folder + f)
    #         except IsADirectoryError:
    #             print(f + ' is a directory.')
    #             pass
    #         except FileNotFoundError:
    #             print(f + ' not found.')
    #             pass
    with open(analysis_folder + title,'a') as f:
        f.write('Unigrams:\t\tBigrams:\t\tTrigrams:\n\n')
        gram_count = 0
        while gram_count < 20:
            unigram = analysis['unigrams'][gram_count]
            bigram = analysis['bigrams'][gram_count]
            trigram = analysis['trigrams'][gram_count]
            output_phrase = unigram + '\t\t' + bigram + '\t\t' + trigram + '\n'
            f.write(output_phrase)
            gram_count += 1
        f.write('\n\nJob post(s):\n\n')
        for jd in jds:
            f.write(jd)

def jd_transcriber(jd_text,title):
    jd_folder = './input/jds/'
    files = os.listdir(path=jd_folder)
    if len(files) > 0:
        for f in files:
            try:
                os.remove(jd_folder + f)
            except IsADirectoryError:
                print(f + ' is a directory.')
                pass
            except FileNotFoundError:
                print(f + ' not found.')
                pass

    with open('./input/jds/' + title + '.txt', 'a') as f:
        f.write(jd_text)
