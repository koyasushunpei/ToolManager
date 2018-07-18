def output(row, form):
    if(form):
        print("{0}:".format(row[0].replace("%2C", ',')))
        print("\tSummary: {0}".format(row[1].replace("%2C", ',')))
        print("\tURL    : {0}".format(row[2].replace("%2C", ',')))
        print("\tDate   : {0}".format(row[3].replace("%2C", ',')))
        print("\tComment: {0}".format(row[4].replace("%2C", ',')))
        print("\tKeyword: {0}".format(row[5].replace("%2C", ',')))
        print("--------------------------------------------------------")
    else:
        print("{0}\t: {1}".format(row[0].replace("%2C", ','), row[1].replace("%2C", ',')))
