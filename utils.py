# Resumationator
#
# Copyright (C) 22022 Jeff Stock
# Author: Jeff Stock <jantonstock@gmail.com>
# For license information, see LICENSE.TXT

"""
DOCSTRING
"""
import vars
import os
import csv


from PyPDF2 import PdfFileReader
from nltk.tokenize import WhitespaceTokenizer

def pdfParser(filename, pageNumber):
        filePath = vars.devFilesPath + filename
        with open(filePath,'rb') as file:
            reader = PdfFileReader(file)
            pdfContents = reader.getPage(pageNumber).extractText()
            return pdfContents

def txtParser(filename):
    filePath = vars.devFilesPath + filename
    with open(filePath) as file:
        txtContents = file.read()
        return txtContents

def create_working_dict(fileLocation):
	compiledList = csv.reader(open(fileLocation, mode='r', encoding='utf-8-sig'))

	dictList = {}
	key = 0

	for v in compiledList:
	   dictList[key] = v
	   key += 1

	headers = dictList[0]

	del dictList[0]

	labeled = {}
	labeledCounter = 1

	for i in dictList:
		pair = {}
		x = 0
		while x < len(headers):
			k = headers[x]
			v = dictList[i][x]
			pair[k] = v
			x += 1
		labeled[labeledCounter] = pair
		labeledCounter += 1

	return labeled

def create_csv(generator,filename):
	output = []
	headers = []
	for i in generator:
		for a in generator[i].keys():
			if a not in headers:
				headers.append(a)

	output.append(headers)

	for x in generator:
		ind = []
		for b in generator[x].values():
			ind.append(b)
		output.append(ind)

	output_path =  vars.devFilesPath + filename + '.csv'

	with open(output_path, 'w') as csvFile:
		writer = csv.writer(csvFile)
		writer.writerows(output)

def harvardKeyworder(wordlist):
    tk = WhitespaceTokenizer()
    tokens = tk.tokenize(wordlist)
    output = []
    for t in tokens:
        output.append([t])
    output_path = vars.devFilesPath + 'harvard_tokens.csv'
    with open(output_path, 'w') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(output)
