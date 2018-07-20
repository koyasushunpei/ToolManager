def output(row, form):
    output_row = []
    for column in row:
        output_row.append(column.replace("%2C", ','))

    if(form):
        print("{0}:".format(output_row[0]))
        print("\tSummary: {0}".format(output_row[1]))
        print("\tURL    : {0}".format(output_row[2]))
        print("\tDate   : {0}".format(output_row[3]))
        print("\tComment: {0}".format(output_row[4]))
        print("\tKeyword: {0}".format(output_row[5]))
        print("--------------------------------------------------------")
    else:
        print("{0}\t: {1}".format(output_row[0], output_row[1]))
