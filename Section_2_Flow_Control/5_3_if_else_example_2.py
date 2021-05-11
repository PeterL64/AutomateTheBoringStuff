print ('Enter a name.')
name = input()
if name:
    print ('Thank you for entering your name.')
else:
    print('You have not entered a name.')

# The name variable is whatever the user inputs, so if name: is True if a
# name is entered by the user and the code will return "Thank you for entering
# your name."
# If the user does not input anything after being prompted to, the variable name
# having no value is a False statement, so the code will return the "else"
# statement; "You have not entered a name."

# This code was for example purposes and is not intuiative. it would be better
# to change the "if name:" line to "if name != '':" ie "if name does not equal
# the blank string" (two single quote marks together, no space)

# Nothing typed is a False value.
# Zero is a False value. You can check with the bool function (Boolean)
# bool(0) Returns False
# bool(1258) Returns True
# Same with string values.
# bool('Hello') Returns Hello
# bool() or bool('') Returns False
