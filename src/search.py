import csv
from src.output import output
import re

def search(word, form):
    print("========================================================")
    print("=                     Search tools                     =")
    print("========================================================")

    file = open('data/list.csv', 'r')
    reader = csv.reader(file)
    header = next(reader)

    if(re.search("'", word)):
        word = word.replace("'", "")
    if(re.search('"', word)):
        word = word.replace('"', "")


    match_counter = 0 # number of tools caught on search
    for row in reader:
        for column in row:
            match = re.search(word, column)
            if match:
                output(row, form)
                match_counter += 1
                break

    if(match_counter):
        print("Hit {0} tools!".format(match_counter))
    else:
        print('No tool matched for "{0}"'.format(word))
