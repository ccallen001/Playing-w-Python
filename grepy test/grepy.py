#! /Library/Frameworks/Python.framework/Versions/3.6/bin/python3

"""
Search Files for Text

usage:
    provide a regexp string as a command line arg,
    search all files in cwd for that regexp
"""

from sys import argv
import os
import re

if len(argv) != 2:
    print("! Please provide 1 regexp string as command line arg")
    quit()

regexp = re.compile(argv[1])
matches = []

for fl in os.listdir():
    openedFile = open(fl, 'r')

    if re.search(regexp, openedFile.read()):
        matches.append(openedFile.name)

    openedFile.close()

if len(matches) == 0:
    print("No files matched the pattern :(")
else:
    print(matches)
