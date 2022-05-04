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

import vars

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
        self.ln(20)


    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')
