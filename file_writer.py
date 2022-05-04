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

from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.person = vars.dev_person
        self.image('./dev/visual/HiredLabs-Icon.png',x=91, y=8, h=7)
        self.image('./dev/visual/HiredLabs-Icon.png',x=121, y=8, h=7)
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

    def add_role(self, org, title, user_input_df):
        is_org = user_input_df['Organization'] == org
        one_org = user_input_df[is_org]
        is_role = one_org['Title'] == title
        role = one_org[is_role]

        start_month = role['Start Month'].unique()[0]
        start_year = role['Start Year'].unique()[0]
        end_month = role['End Month'].unique()[0]
        end_year = role['End Year'].unique()[0]

        start_date = '{} {}'.format(start_month, start_year)
        end_date = '{} {}'.format(end_month, end_year) if end_month != 'None' and end_year != 'None' else 'Present'
        dates = '{} - {}'.format(start_date,end_date)

        role_bullets = utils.role_bullet_prepper(user_input_df, org, title)

        self.set_font('Times','B', size=11)
        self.cell(w=100, h=5, txt=title,ln=0,align='L')
        self.set_font('Times', size=11)
        self.cell(w=80, h=5, txt=dates, ln=1, align='R')
        self.ln(1)
        self.cell(w=15, h=5,ln=0)
        self.multi_cell(165, 5, role_bullets, 0, 'L')
        self.ln(h=3)

    def add_resume_org(self, org, user_input_df):
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
            self.add_role(org, title, user_input_df)

    def add_resume_section(self, section_type, user_input_df):
        section_title = 'Experience' if section_type == 'Work' else 'Education'
        self.set_font('Times','B', size=11)
        self.cell(w=200, h=5, txt=section_title, ln=1, align='C')
        is_work_exp = user_input_df['Type'] == 'Work'
        work_exp =  user_input_df[is_work_exp]
        date_sorted_orgs = work_exp.sort_values(by=['iso_start_date'], ascending=False)
        unique_orgs = date_sorted_orgs['Organization'].unique()
        for org in unique_orgs:
            self.add_resume_org(org, user_input_df)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')