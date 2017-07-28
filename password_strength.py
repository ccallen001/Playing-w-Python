"""Password Strength Checker"""

import pyperclip
import re
import sys


def main():

    try:
        pw = sys.argv[1]
    except IndexError:
        print("Please provide a password through the command line.")
        quit()

    length = re.compile('\w{8}')
    down = re.compile('[a-z]')
    up = re.compile('[A-Z]')
    dig = re.compile('\d')

    checks = [length, down, up, dig]

    matchList = []

    for check in checks:
        valid = check.search(pw)
        if valid:
            matchList.append(valid)

            what = 'how?'

    if len(matchList) == 4:
        print("Valid password! :)")
    else:
        print("Make it stronger. :(")

main()
