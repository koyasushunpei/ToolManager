import csv
import src.check as check
import src.output as output

def delete(tool_name):
    print("========================================================")
    print("=                     Delete tool                      =")
    print("========================================================")
    print("")
    # file = open("data/list.csv", "r")
    # reader = csv.reader(file)
    # header = next(reader)
    # file_exist = False
    # for row in reader:
    #     if(row[0] == tool_name):
    #         output.output(row, True)
    #         file_exist = True
    #         break
    # if not(file_exist):
    #     print("Can't find {0}".format(tool_name))
    #     exit(0)
    check.check(tool_name, True) # output True

    print("========================================================")
    print("=                       WARNING                        =")
    print("========================================================")
    answer = input("Are you sure to delete {0} from your list? [yN]".format(tool_name))
    if not(answer == "Y" or answer == "y"):
        exit(0)
    answer = input("OK? [yN]")
    if not(answer == "Y" or answer == "y"):
        exit(0)


    file = open('data/list.csv', 'r+')
    lines = file.readlines()
    file.seek(0)
    for line in lines:
        if(line.split(",")[0] != tool_name):
            file.write(line)
    file.truncate()
    file.close()


def delete_by_update(tool_name):
    file = open('data/list.csv', 'r+')
    lines = file.readlines()
    file.seek(0)
    for line in lines:
        if(line.split(",")[0] != tool_name):
            file.write(line)
    file.truncate()
    file.close()

