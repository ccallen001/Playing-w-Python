"""reimplementation of the strip method"""

import re


def main():
    '''main function'''
    def stripIt(string, seqToStrip):
        '''strip function'''
        if not seqToStrip:
            print(re.compile(r'^\s+').sub('', string))
            # not sure how to get the end whitespace /s+?
        else:
            print(re.compile(seqToStrip).sub('', string))
    string = raw_input("String to strip?\n> ")
    seqToStrip = raw_input("Sequence to remove?\n> ")

    stripIt(string, seqToStrip)
main()
