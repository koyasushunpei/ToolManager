#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import os
from src.add import add # original
from src.dump import dump # original
from src.export import export #original
from src.import_file import import_file # original
from src.delete import delete # original
from src.keyword import keyword, dumpkey # original
from src.search import search # original
from src.update import update # original


def main():
    os.chdir(os.path.dirname(__file__)) # dirctory setting

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
    parser.add_argument('-e', '--export', action='store_true', help='export tool list to html file')
    parser.add_argument('-k', '--keyword', action='store', help='filter by keyword')
    parser.add_argument('-l', dest='form', action='store_true', help='dump tools with full information')
    parser.add_argument('-s', '--search', dest='word', action='store', help='search tools with reguler expression')
    parser.add_argument('-u', '--update', dest='updatetoolname', action='store', help='update tool information')

    args = parser.parse_args()

    if not any(vars(args).values()):
        parser.error('No arguments provided.')
        exit(0)

    if(args.deletetoolname):
        delete(args.deletetoolname)
    elif(args.dump):
        dump(args.form)
    elif(args.dumpkey):
        dumpkey()
    elif(args.infile):
        import_file(args.infile)
    elif(args.add):
        add()
    elif(args.keyword):
        keyword(args.keyword, args.form)
    elif(args.word):
        search(args.word, args.form)
    elif(args.updatetoolname):
        update(args.updatetoolname, args.form)
    elif(args.export):
        export()


if __name__ == '__main__':
    main()
