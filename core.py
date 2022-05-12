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


from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch

def page_maker():
    doc = SimpleDocTemplate(
        './dev/tailored_resumes/demo_platypus.pdf',
        pagesize=letter,
        # rightMargin=72, leftMargin=72,
        # topMargin=72, bottomMargin=18,
    )

    styles = getSampleStyleSheet()
    flowables = []
    spacer = Spacer(1, 0.25 * inch)
    for i in range(25):
        text = 'Hello, I am a paragraph.'
        para = Paragraph(text,style=styles['Normal'])
        flowables.append(para)
        flowables.append(spacer)

    doc.build(flowables)

if __name__ == '__main__':
    page_maker()
