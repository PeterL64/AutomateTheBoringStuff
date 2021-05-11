name = ''
while True:
    print('Please enter your name.')
    name = input()
    if name == 'your name':
        break
print ('Thank you.')

# "While True" is an infinite loop that will print "Please enter your name"
# followed by a prompt for you to type your name.
# This program will keep looping until you literally type "your name"
# This program will never be False because True always evaluates to True. So it
# will keep running until the "if statement" becomes true, which executed the
# "break" function.
