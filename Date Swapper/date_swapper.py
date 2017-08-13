#! python3

"""Date swaper for swapping dates from US to EU"""

import os
import re
import shutil


def main():
    """main function"""

    for fl in os.listdir():
        pat = re.compile(r'\d\d-\d\d-\d\d\d\d')

        if re.search(pat, fl):
            start = re.search(pat, fl).span()[0]
            split = fl[start:start + 10].split('-')
            shutil.move(fl, '{0}-{1}-{2}'.format(split[1], split[0], split[2]))

main()
