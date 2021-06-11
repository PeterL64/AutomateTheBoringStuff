import random

def getAnswer(AnswerNumber):
    if AnswerNumber == 1:
        return 'It is certain'
    elif AnswerNumber == 2:
        return 'It is possible'
    elif AnswerNumber == 3:
        return 'Yes'
    elif AnswerNumber == 4:
        return 'Try again'
    elif AnswerNumber == 5:
        return 'Nah Mate'
    elif AnswerNumber == 6:
        return 'Ho Ho Ho, not a hope'

print('Think of a yes/no question, and press enter to see what random answer you will get.')
input()

print(getAnswer(random.randint(1, 6)))

# This is a program where you can make up a random Y/N question in your head, and
# the program will give you an answer for it.

# We defined the function getAnswer that has a parameter called AnswerNumber.
# In the block of code, if the parameter is equal to certain values we have
# programmed it to print a string answer.

# Now when the program is ran it will print asking you to press enter.
# Next line will ask the user for input. We did not constrict the user's input
# so they technically can enter anything and press enter.
# The last line will get a random integer between 1 and 6, assign that number to
# the function getAnswer, i.e. it will be the function's new parameter. Finally,
# it will print the corresponding return value.
