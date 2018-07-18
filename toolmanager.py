#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import src.add as add # original
import src.dump as dump # original
import src.import_file as import_file # original
import src.delete as delete # original
import src.keyword as keyword # original
import src.search as search # original
import src.update as update # original


def main():
    parser = argparse.ArgumentParser(
        prog='toolmanager.py',
        usage='./toolmanager.py [options]',
        description='',
        epilog='',
        add_help=True,
    )
    parser.add_argument('--delete', dest='deletetoolname', action='store', help='delete tool from list')
    parser.add_argument('--dump', action='store_true', help='dump tools')
    parser.add_argument('--dumpkey', action='store_true', help='dump all keywords')
    parser.add_argument('--import', dest='infile', action='store', help='import tool list from csv file')
    parser.add_argument('-a', '--add', action='store_true', help='add new tool')
    parser.add_argument('-k', '--keyword', action='store', help='filter by keyword')
    parser.add_argument('-l', dest='form', action='store_true', help='dump tools with full information')
    parser.add_argument('-s', '--search', dest='word', action='store', help='search tools with reguler expression')
    parser.add_argument('-u', '--update', dest='updatetoolname', action='store', help='update tool information')

    args = parser.parse_args()

    if not any(vars(args).values()):
        parser.error('No arguments provided.')
        exit(0)

    if(args.deletetoolname):
        delete.delete(args.deletetoolname)
    elif(args.dump):
        dump.dump(args.form)
    elif(args.dumpkey):
        keyword.dumpkey()
    elif(args.infile):
        import_file.importFile(args.infile)
    elif(args.add):
        add.add()
    elif(args.keyword):
        keyword.keyword(args.keyword, args.form)
    elif(args.word):
        search.search(args.word, args.form)
    elif(args.updatetoolname):
        update.update(args.updatetoolname, args.form)


if __name__ == '__main__':
    main()
