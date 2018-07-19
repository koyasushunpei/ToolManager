import csv
from src.output import output

def check(tool_name, flag):
    file = open("data/list.csv", "r")
    reader = csv.reader(file)
    header = next(reader)
    file_exist = False
    for row in reader:
        if(row[0] == tool_name):
            if(flag):
                output(row, True) # full information
            file_exist = True
            break
    if not(file_exist):
        print("Can't find '{0}'".format(tool_name))
        exit(0)
