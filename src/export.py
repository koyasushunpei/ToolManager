import csv
import os

def export():
    file = open('data/list.csv', 'r')
    reader = csv.reader(file)
    header = next(reader)

    outfile = open('data/list.html', 'w')

    firstline = "<h1>Tool List</h1>\n\n\n"
    firstline += "<link rel='stylesheet' type='text/css' href='list.css'>\n"
    outfile.write(firstline)

    for row in reader:
        out_row = "<hr>"
        out_row += "<h2>{0}</h3>\n".format(row[0])
        out_row += "<h5>\n"
        out_row += "<div>\n"
        out_row += "<span class='col-1'>Summary</span>\n"
        out_row += "<span class='col-2'>: {0}</span>\n".format(row[1])
        out_row += "</div>\n"
        out_row += "<div>\n"
        out_row += "<span class='col-1'>URL</span>\n"
        out_row += "<span class='col-2'>: <a href={0}>{0}</a></span>\n".format(row[2])
        out_row += "</div>\n"
        out_row += "<div>\n"
        out_row += "<span class='col-1'>Date</span>\n"
        out_row += "<span class='col-2'>: {0}</span>\n".format(row[3])
        out_row += "</div>\n"
        out_row += "<div>\n"
        out_row += "<span class='col-1'>Comment</span>\n"
        out_row += "<span class='col-2'>: {0}</span>\n".format(row[4])
        out_row += "</div>\n"
        out_row += "<div>\n"
        out_row += "<span class='col-1'>Keyword</span>\n"
        out_row += "<span class='col-2'>: {0}</span>\n".format(row[5])
        out_row += "</div>\n"
        out_row += "</h5>\n"

        outfile.write(out_row)

    print("open file://%s in your browser" % (os.path.abspath("data/list.html")))
