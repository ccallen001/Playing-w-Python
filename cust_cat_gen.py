#!/usr/bin/env python

"""This program generates the 3 files
required for SHQ custom categories.
"""

import os

print("""
                            _,.--.
        --..,_           .'`__ o  `;__,
           `'.'.       .'.'`  '---'`  '          
              '.`-...-'.'
                `-...-'

----------------------
CUSTOM CATEGORY GENERATOR
-------------------------

Welcome! Ready for fun??

- ensure you have 3 existing cat/prod files
in the same directory/folder as this program

- Hit 'crtl + c' on your keyboard to abort
and move files if necessary

- If you're ready to go.. hit 'enter' on your keyboard""")
raw_input("> ")

print("What's the new category name?")
cat_name = raw_input("> ")

print("What's the file naming convention for category?")
cat_file = raw_input("> ").replace(".txt", '')
print("For category relations?")
cat_relations_file = raw_input("> ").replace(".txt", '')
print("For category product relations?")
cat_prod_relations_file = raw_input("> ").replace(".txt", '')

os.chdir('../../Users/callen/Desktop/Custom Category Generator')

for f_name in [cat_file, cat_relations_file, cat_prod_relations_file]:
    for fl in os.listdir('.'):
        # print(fl)
        if fl.endswith('{}.txt'.format(f_name)):
            read = open(fl, 'r')
            write = open('{}_{}.txt'.format(cat_name, f_name), 'w')
            write.write(read.readline())
            for f in [read, write]:
                f.close()
