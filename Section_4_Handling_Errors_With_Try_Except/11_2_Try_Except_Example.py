print('How many cats do you have?')  # Here is asks how many cats you have
numCats = input()  # The user can type in how many they have and it is assigned
# to numCats Variable
if int(numCats) >= 4:  # input returns a string value that must be converted with int, then compared to the number 4.
    print('That is a lot of cats.')  # If it is True print this string
else:  # Or else print this different string
    print('That is not that many cats.')

# The problem with this code is the user can type anything into it. For example
# a user could type their answer instead of pressing a number key. Since the
# program is expecting to change an integer(number) to a string, this will
# cause an error.


# Use try and except to solve this issue:
print('How many cats do you have?')
NumCats = input()
try:
    if int(NumCats) >= 4:
        print('That is a lot of cats.')
    else:
        print('That is not that many cats.')
except ValueError:
    print('You did not enter a number.')

# Try to figure out code to detect when a user inputs a negative number and
# display an error message for them.


print('How many cats do you have?')
NumCats = input()
try:
    if int(NumCats) >= 4:
        print('That is a lot of cats.')
    elif int(NumCats) < 0:  # else if number < 0
        print('You cannot have negative cats')
    else:
        print('That is not that many cats.')
except ValueError:
    print('You did not enter a number.')
