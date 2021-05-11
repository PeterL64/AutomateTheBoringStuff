name = ''
while name != 'your name':
    print('Please enter your name')
    name = input()
print('Thank you')

# The name variable has been set to the blank string.
# This makes the next line True because a blank string does not equal the string
# "your name". So while the 'WHILE' the condition is True, it loops back to the
# beginning of the loop. And the code prints "Please enter your name".

# Now the program is waiting for us to enter a value for name.
# When you enter a name the program returns "Please enter your name". This is
# because the string value you entered, "Peter", does not equal " your name",
# so the statement is still True and the WHILE loop loops around and runs again.

# When you eventually type "your name", the statement "name != 'your name' is now
# False. This is because the variable 'name' is now set to the string "your name",
# which IS equal to the string "your name". So the condition is now False and the
# loop stops running and moves on to the next part of the code and prints
# "Thank you"



# If you ever have an infinite loop error, where the code keeps looping forever
# press ctrl + c to stop the loop from running.
# This causes a keyboard interrupt error and crashes your program stopping it.
