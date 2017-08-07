#! python3

"""randomQuizGenerator.py - Creates quizzes with questions and answers in
random order, along with the answer key."""

import random

statesAndCaps = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
                 'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
                 'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
                 'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
                 'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
                 'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
                 'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
                 'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
                 'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
                 'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton',
                 'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
                 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
                 'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
                 'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
                 'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City',
                 'Vermont': 'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia',
                 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

numOfQuizzes = 2

for i in range(numOfQuizzes):
    shuffledStates = list(statesAndCaps.keys())
    random.shuffle(shuffledStates)
    shuffledCaps = list(statesAndCaps.values())
    random.shuffle(shuffledCaps)

    iP1 = i + 1

    quiz = open('Quiz' + str(iP1), 'w')
    quiz.write('Quiz %s:\n\n' % str(iP1))
    key = open('Key' + str(iP1), 'w')
    key.write('Key %s:\n\n' % str(iP1))

    for j, state in enumerate(shuffledStates):
        copiedCaps = shuffledCaps[:]
        rightAnswer = statesAndCaps[state]
        del copiedCaps[copiedCaps.index(rightAnswer)]
        wrongAnswers = random.sample(copiedCaps, 3)

        wrongAnswers.append(rightAnswer)
        possibleAnswers = wrongAnswers
        random.shuffle(possibleAnswers)

        quiz.write("""{0}. What is the capital of {1}?
            
    a) {2[0]}

    b) {2[1]}

    c) {2[2]}

    d) {2[3]}

""".format(j + 1, state, possibleAnswers))

        choices = ['a', 'b', 'c', 'd']

        key.write('{0}: {1}\n'.format(
            j + 1, choices[possibleAnswers.index(rightAnswer)]))

    quiz.close()
    key.close()
