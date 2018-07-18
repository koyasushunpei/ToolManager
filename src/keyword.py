import csv
import src.output as output

def dumpkey():
    print("========================================================")
    print("=                  Dump all keywords                   =")
    print("========================================================")

    file = open('data/list.csv', 'r')
    reader = csv.reader(file)
    hedear = next(reader)

    keywords = {}

    for row in reader:
        keyword_in_column = row[5].split(" ")
        for keyword in keyword_in_column:
            if(keyword not in keywords):
                keywords[keyword] = 1
            else:
                keywords[keyword] += 1

    for key, value in sorted(keywords.items(), key=lambda x: -x[1]):
        print("{0}\t: {1}".format(key, value))


def keyword(word, form):
    print("========================================================")
    print("=                  Filter by keywords                  =")
    print("========================================================")

    file = open('data/list.csv', 'r')
    reader = csv.reader(file)
    hedear = next(reader)

    match_counter = 0

    for row in reader:
        if(word in row[5].split(" ")):
            output.output(row, form)
            match_counter += 1


    if(match_counter):
        print("Hit {0} tools!".format(match_counter))
    else:
        print('No tool matched for "{0}"'.format(word))
