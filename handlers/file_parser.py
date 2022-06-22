import os
import pandas as pd
from PyPDF2 import PdfFileReader

# Reads file names from a directory and makes a string with the relative
# path to each file in a list.
def corpus_prepper(corpus: str) -> list[str]:
    jds = os.listdir(path=corpus)
    print(jds)
    return [corpus + jd for jd in jds]

# pulls text from a .txt file
def txt_parser(filename: str) -> list:
    with open(filename) as file:
        txtContents = file.read()
        return txtContents

# pulls the text out of a pdf
def pdf_parser(filename, pageNumber):
        filePath = vars.devFilesPath + filename
        with open(filePath,'rb') as file:
            reader = PdfFileReader(file)
            pdfContents = reader.getPage(pageNumber).extractText()
            return pdfContents


# takes in a .csv file and returns a pandas data frame object.
def csv_to_df(filename):
    csv_in = pd.read_csv(filename)
    working = pd.DataFrame(csv_in)

    return working
