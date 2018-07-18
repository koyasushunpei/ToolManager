import csv
import src.output as output
import subprocess

def dump(form):
    filename = "data/list.csv"

    number_of_tools = len(open(filename).readlines())
    file = open(filename, 'r')

    reader = csv.reader(file)
    header = next(reader)
    print("========================================================")
    print("=                    Dump all tools                    =")
    print("========================================================")


    if(number_of_tools >= 50):
        print("There are many tools in the list")
        answer = input("Are you sure to dump all the tools? [yN]")
        if not(answer == "Y" or answer == "y"):
            exit(0)

    for row in reader:
        output.output(row, form)
