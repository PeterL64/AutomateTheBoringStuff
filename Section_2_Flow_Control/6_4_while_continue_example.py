spam = 0
while spam < 5:
    spam = spam + 1
    if spam == 3:
        continue
    print('spam is ' + str(spam))

# spam is equal to 0. While spam is less than 5, add 1 to it and print "spam is
# (whatever number it happens to be).
# This prints "spam is 1", "spam is 2", "spam is "4, "spam is 5", skipping 3.
# This is because due to the if statement, as soon as the loop reaches spam = 3,
# the program function continue executes and returns to the beginning or the loop,
# skipping whatever code was below is, in this case the print function.

# continue function immediately stops the loop and returns to the beginning.

# The str(spam) is to change the integer value of spam to a string so that we can
# add the two strings together.
