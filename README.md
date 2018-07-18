# ToolManager
__Tool list management tool__

# Usage
```
./toolmanager.py -h
usage: ./toolmanager.py [options]

optional arguments:
  -h, --help            show this help message and exit
  --delete DELETETOOLNAME
                        delete tool from list
  --dump                dump tools
  --dumpkey             dump all keywords
  --import INFILE       import tool list from csv file
  -a, --add             add new tool
  -k KEYWORD, --keyword KEYWORD
                        filter by keyword
  -l                    dump tools with full information
  -s WORD, --search WORD
                        search tools with reguler expression
  -u UPDATETOOLNAME, --update UPDATETOOLNAME
                        update tool information
```

### get (all information about) tool information in the list
```
./toolmanager.py --dump (-l)
```
### add new tool to list
```
./toolmanager.py -a
```
### search for tool by your input
```
./toolmanager.py -s WORD # you can use reguler expression
```
### filter tool by keyword
```
./toolmanager.py -k KEYWORD (-l)
```
### dump all keywords
```
./toolmanager.py --dumpkey (-l)
```
### update tool information
```
./toolmanager.py -u TOOLNAME
```
### delete tool from list
```
./toolmanager.py --delete TOOLNAME
```

# Files
Tool information stores in data/list.csv.  
__Do not modify or delete this file!!__

Main function is in toolmanager.py and other functions are in src/ directory



# TODO
(Clean function)
