import csv
import datetime
from src.output import output

def getToolInfo():
    print("========================================================")
    print("=                   Update tool list                   =")
    print("========================================================")
    print("Input following infomation")
    print("")

    # Tool Name
    tool_name = input("Name of the tool\t: ")
    for i in range(3): # max umber of input checks
        if(len(tool_name) == 0):
            tool_name = input("write something\t: ")
        else:
            break
    # Check for duplicates
    file = open('data/list.csv', 'r')
    reader = csv.reader(file)
    header = next(reader)

    for row in reader:
        if(row[0] == tool_name):
            print("{0} is already exists in your list".format(tool_name))
            print("--------------------------------------------------------")
            output(row, True) # output full information
            exit(0)



    # Tool Overview
    tool_overview = input("Summary of {0}\t: ".format(tool_name))
    for i in range(3): # max umber of input checks
        if(len(tool_overview) == 0):
            tool_overview = input("write something\t: ")
        else:
            break

    # URL
    while(True):
        tool_url = input("Related URLs for {0}\t: ".format(tool_name))
        if(tool_url.find("http") != -1):
            break
        else:
            answer = input("Is it URL? Do you want to type again? [yN]")
            if not(answer == "Y" or answer == "y"):
                break


    # Date
    tool_date = datetime.date.today()

    # Comment
    tool_comment = input("Comment about {0}, if you need\t: ".format(tool_name))

    # keywords
    tool_keyword = input("Keywords (seperate by single space)\t: ")

    return tool_name, tool_overview, tool_url, str(tool_date), tool_comment, tool_keyword


def add():
    new_tool = getToolInfo()

    for column in new_tool:
        column = column.replace(",", "%2C")

    file = open('data/list.csv', 'a')
    writer = csv.writer(file, lineterminator='\n')
    writer.writerow(new_tool)

    file.close()
