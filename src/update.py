import csv
import datetime
import src.delete as delete
import src.output as output

def modify(modify_tool, new_tool, header, index):
    # tool name should not change
    column_name = header[index]

    if(column_name == "Name"):
        new_tool.append(modify_tool[index])
        return
    if(column_name == "Date"):
        new_tool.append(str(datetime.date.today()))
        return
    answer = input("Do you want to change {0}? [yN]".format(column_name))
    if not(answer == "Y" or answer == "y"):
        new_tool.append(modify_tool[index])
        return
    else:
        if(column_name == "URL"):
            while(True):
                new_info = input("Input new information about {0}\t: ".format(column_name))
                if(new_info.find("http") != -1):
                    break
                else:
                    answer = input("Is it URL? Do you want to type again? [yN]")
                    if not(answer == "Y" or answer == "y"):
                        break

        else:
            new_info = input("Input new information about {0}\t: ".format(column_name))

    new_tool.append(new_info.replace(",", "%2C"))


def update(tool_name, form):
    print("========================================================")
    print("=               Update tool information                =")
    print("========================================================")
    file = open('data/list.csv', 'r')
    reader = csv.reader(file)
    header = next(reader)

    modify_tool = []
    new_tool = []

    file_exist = False
    for row in reader:
        if(row[0] == tool_name):
            modify_tool = row
            output.output(row, True)
            file_exist = True
            break

    if not(file_exist):
        print("Can't find '{0}'".format(tool_name))
        exit(0)

    for index in range(sum(1 for _ in header)):
        modify(modify_tool, new_tool, header, index)

    file.close()

    for column in new_tool:
        column = column.replace(",", "%2C")

    delete.delete_by_update(tool_name)

    file = open("data/list.csv", 'a')
    writer = csv.writer(file, lineterminator='\n')
    writer.writerow(new_tool)
