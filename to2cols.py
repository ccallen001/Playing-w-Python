"""To 2 Cols"""

#-------------------------------------------------------------------------------

from sys import argv

termcolorErr = False
try:
    from termcolor import colored
except ImportError:
    termcolorErr = True
    print('Could not import termcolor. :/ Oh well.')

#-------------------------------------------------------------------------------

print('\n----------\n  3 -> 2  \n----------\n')

try:
    srcFileName = argv[1]

    srcFile = open(srcFileName, 'r')
    contents = srcFile.read()
    rows = contents.split('\n')
    newRows = []

    srcFileDelimeter = 'X'
    while srcFileDelimeter not in ',|t':
        print('What\'s the delimeter?\nType: \',\' \'|\' or \'t\'.')
        srcFileDelimeter = raw_input('> ')
        print(srcFileDelimeter)
    delDict = {',': ',', '|': '|', 't': '\t'}

    delWhichCol = 'X'
    while delWhichCol not in '123':
        print('Delete which column?\nType: \'1\' \'2\' or \'3\'.')
        delWhichCol = raw_input('> ')

    destFileName = ''
    while destFileName == '':
        print('What do you want the output file to be named?')
        destFileName = raw_input('> ')

    for row in rows:
        row = row.replace('\r', '')
        newRow = row.split(delDict[srcFileDelimeter])
        del newRow[int(delWhichCol) - 1]
        if len(newRow) == 2:
            newRows.append(
                newRow[0] + delDict[srcFileDelimeter] + newRow[1] + '\r\n')

    joined = ''.join(newRows)

    try:
        twoCol = open(destFileName + '.txt', 'w')
    except:
        if not termcolorErr:
            print colored('Could not write file %s. :(' % destFileName, 'red')
        else:
            print('Could not write file % s.: (' % destFileName)

    if not termcolorErr:
        print colored('Writing {}...'.format(destFileName), 'yellow')
    else:
        print('Writing {}...'.format(destFileName))

    twoCol.write(joined)

    if not termcolorErr:
        print colored('Done. :)', 'green')
    else:
        print('Done. :)')
except IndexError:
    if not termcolorErr:
        print colored('Please supply filename as a command line arg.', 'red')
    else:
        print('Please supply filename as a command line arg.')
