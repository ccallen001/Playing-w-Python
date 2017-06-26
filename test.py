import random
import string
low = string.ascii_lowercase + ' '

user_inp = raw_input('Give me some text: ').lower()
rnd_str = []

for char in user_inp:
    rnd_str.append(low[random.randint(0, len(low)) - 1])

j = 0
while ''.join(rnd_str) != user_inp and j < 1000:
    i = 0
    for char in user_inp:
        if rnd_str[i] != user_inp[i]:
            rnd_str[i] = low[random.randint(0, len(low)) - 1]
        i += 1
    j += 1
    print '{}: %s'.format(j) % ''.join(rnd_str)

# def add(a, b):
#     print "ADDING %d + %d" % (a, b)
#     return a + b


# def subtract(a, b):
#     print "SUBTRACTING %d - %d" % (a, b)
#     return a - b


# def multiply(a, b):
#     print "MULTIPLYING %d * %d" % (a, b)
#     return a * b


# def divide(a, b):
#     print "DIVIDING %d / %d" % (a, b)
#     return a / b


# print "Let's do some math with just functions!"

# age = add(30, 5)
# height = subtract(78, 4)
# weight = multiply(90, 2)
# iq = divide(100, 2)

# print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)


# # A puzzle for the extra credit, type it in anyway.
# print "Here is a puzzle."

# what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

# print "That becomes: ", what, "Can you do it by hand?"
