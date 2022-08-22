import os
import csv
import pandas as pd
import PyPDF2

from pdfminer.high_level import extract_text

# Reads file names from a directory and makes a string with the relative
# path to each file in a list.
def corpus_prepper(corpus: str) -> list[str]:
    jds = os.listdir(path=corpus)
    return [corpus + jd for jd in jds]

# pulls text from a .txt file
def txt_parser(filename: str) -> list:
    with open(filename) as file:
        txtContents = file.read()
        return txtContents

# pulls the text out of a pdf
def pdf_parser(filepath):
    text = extract_text(filepath)
    return text


# takes in a .csv file and returns a pandas data frame object.
def csv_to_df(filename):
    df = pd.read_csv(filename)

    return df

def csv_to_list(file_location):
    compiled_list = csv.reader(open(file_location, mode='r', encoding='utf-8-sig'))
    output = list()
    for word in compiled_list:
        output.append(word[0])
    return output
