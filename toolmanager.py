#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import src.add as add # original
import src.dump as dump # original
# import src.dumpall as dumpall # original
import src.import_file as import_file # original
import src.keyword as keyword # original
import src.search as search # original


def main():
    parser = argparse.ArgumentParser(
        prog='toolmanager.py',
        usage='./toolmanager.py [options]',
        description='',
        epilog='',
        add_help=True,
    )
    parser.add_argument('--dump', action='store_true', help='dump tools')
    # parser.add_argument('--dumpall', action='store_true', help='dump all fields of all tools')
    parser.add_argument('--dumpkey', action='store_true', help='dump all keywords')
    parser.add_argument('-l', dest='form', action='store_true', help='dump tools with full information')
    parser.add_argument('-a', '--add', action='store_true', help='add new tool')
    parser.add_argument('-s', '--search', action='store', help='search tools with reguler expression')
    parser.add_argument('-k', '--keyword', action='store', help='filter by keyword')
    parser.add_argument('--import', dest='infile', action='store', help='import tool list from csv file')
    args = parser.parse_args()

    if(args.dump):
        dump.dump(args.form)
    # elif(args.dumpall):
    #     dumpall.dumpall()
    elif(args.dumpkey):
        keyword.dumpkey()
    elif(args.add):
        add.add()
    elif(args.search):
        search.search(args.search, args.form)
    elif(args.keyword):
        keyword.keyword(args.keyword, args.form)
    elif(args.infile):
        import_file.importFile(args.infile)




if __name__ == '__main__':
    main()
