import os

def import_file(filename):
    if not(os.path.exists(filename)):
        print("File not exist")
        exit(0)

    print("========================================================")
    print("=                   Import tool list                   =")
    print("========================================================")
    print("")
    answer = input("Are you sure to import {0} to your list? [yN]".format(filename))
    if not(answer == "Y" or answer == "y"):
        exit(0)
    answer = input("It's dangerous!! OK? [yN]")
    if not(answer == "Y" or answer == "y"):
        exit(0)

    infile = open(filename, 'r')
    infile.readline() # delete header

    outfile = open('data/list.csv', 'a')
    outfile.write(infile.read())
