print('Hello') # Print function usually adds a new line to end of the string it prints.
print('World')

# Running the above code will print out Hello and World on two seperate lines.

# However, you can set the end keyword argument to change this to a different
# string other than the new line character.

print('Hello', end='') # The keyword argument end which is equal to the string
print('World')         # value blank, the blank string.

# Now there is no new line after Hello, the new print statement ends up on the
# same line as Hello.






# When you pass multiple strings through the print function, print automatically
# seperates them with a single space. Eg below:
print('cat', 'dog','mouse')

# Use the sep keyword argument, you can change what the seperating character is,
# Eg below:
print('cat', 'dog','mouse', sep='ABCDE')
print('cat', 'dog','mouse', sep='999')
seperation = '22222'
print('cat', 'dog','mouse', sep=seperation)
