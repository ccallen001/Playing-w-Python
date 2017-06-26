"""a program for getting info about files"""

print """

-------------------------------------------------
             Welcome to File Reader!             
-------------------------------------------------

Please make sure you have this program file
in the same directory/folder as the file
about which you want to get info.

If it's currently not in that folder,
then hit CRTL + C to quit and move the program file
"""

print "Please click ENTER on your keyboard to continue"
raw_input("> ")

file_name = None
file_obj = None
read_file = None
def getFile():
    global file_name, file_obj, read_file

    print "What's the name of your file?"
    file_name = raw_input("> ")

    try:
        file_obj = open(file_name, 'r')
        read_file = file_obj.read()
        file_obj.close()
    except:
        print """
        Oops, there was an error.
        Please try again!
        Or.. hit CTRL + C to quit.
        """

        getFile()
getFile()

read_file_list = list(read_file)
char_obj = {}
max_char = None
max_char_count = 0;

for read_char in read_file_list:
    if not (read_char in char_obj) and read_char != ' ':
        char_obj[read_char] = 1
    elif read_char != ' ':
        char_obj[read_char] += 1
        if char_obj[read_char] > max_char_count:
            max_char = read_char
            max_char_count = char_obj[read_char]

print """
File Stats for %s:
-------------------------------------------------""" % file_name
print "Number of lines: %d." % len(read_file.split('\n'))
print "Number of chars: %d." % len(read_file_list)
print "Most frequent char: '%s' -> %d times." % (max_char, max_char_count)
print "-------------------------------------------------\n"

print "Would you like to make a copy of the file? Y or N"
y_or_n = raw_input("> ")

if y_or_n == 'Y' or y_or_n == 'y':
    open('copy-' + file_name, 'w').write(open(file_name, 'r').read())

print "Thank you, all done!\n"
