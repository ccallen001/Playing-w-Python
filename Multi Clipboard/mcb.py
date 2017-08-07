"""Multi Clipboard

usage (command line args):
    save <key> - saves a new '<key>': '<contents of clipboard>' pair
    delete <key> - deletes the key value pair associated with <key>
    list - lists key value pairs
    <key> - copies value of <key> to clipboard
"""

from sys import argv
import shelve
import pyperclip

mcbShelf = shelve.open('mcb')

if len(argv) == 1:
    print("! Please provide command line argument:\n'save', 'list', or <key>")
else:
    if argv[1].lower() == 'save' or argv[1].lower() == 'delete':
        if not argv[2]:
            print("! Please provide a key/variable as 2nd command line arg")
        elif argv[1].lower() == 'save':
            mcbShelf[argv[2]] = pyperclip.paste()
        else:
            if argv[2] not in mcbShelf:
                print(
                    "! %s not found in list of keys. Use 'list' to print keys" % argv[2])
            else:
                del mcbShelf[argv[2]]
    elif argv[1].lower() == 'list':
        for key in mcbShelf.keys():
            print("{0}: {1}".format(key, mcbShelf[key]))
    else:
        if argv[1] not in mcbShelf:
            print("! %s not found in list of keys. Use 'list' to print keys" %
                  argv[1])
        else:
            pyperclip.copy(mcbShelf[argv[1]])

mcbShelf.close()
