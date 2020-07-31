import re
import os
import glob
import csv

from bs4 import BeautifulSoup as bs

import json

import xml.etree.ElementTree as ET

path = os.getcwd()
target = 'Training-Set-2018/'

entries = os.listdir(target)

for entry in entries:
    if entry == 'FilterSent':
        continue
    temPath = path + '/' + target + entry + '/Reference_XML/'
    print(temPath)
    temPath2 = glob.glob(temPath + '*.xml')[0]
    print(temPath2)
    filename = temPath2.split('/')[-1]
    print(temPath2)
    print(filename)

    # print(inputFile)
    outpath = temPath + filename.rstrip(".xml") + ".csv"
    print(outpath)

    cnt = 0
    with open(outpath, 'w', newline='')as f:
        thewriter = csv.writer(f)
        listRow = ['id', 'sentence']
        thewriter.writerow(listRow)

        file = temPath2

        with open(file, encoding='latin') as f:

            text = f.read()

        # creating an object of BeautifulSoup with text of xml file

        soup = bs(text, "lxml")

        # initializing an empty dictionary

        data = {}

        # reading title of papaer and adding it to the dictionary.

        data["paper_title"] = bs(text[text.find("<PAPER>") + 7:text.find("<ABSTRACT>")].strip(), "lxml").text

        # reading abstract

        # some of the paper don't have abstract

        # error handling is required in those cases

        try:
            abstract = soup.find("abstract")
            a = abstract.findAll("s")
            a_texts = list(map(lambda i: i.text.strip(), a))
            for each in a_texts:
                thewriter.writerow([cnt, each])
                cnt = cnt + 1



        except AttributeError:
            data["abstract"] = ""

        # finding all other sections like Introduction ... Conclusion.

        sections = soup.findAll("section")

        # Iterating through the sections and

        # creating a list of lines corresponding to each sentences in the section

        for section in sections:

            s = section.findAll("s")

            s_texts = list(map(lambda i: i.text.strip(), s))

            data[section.attrs["title"].strip()] = s_texts
            for each in s_texts:

                if len(each) > 15:
                    thewriter.writerow([cnt, each])
                    cnt = cnt + 1


