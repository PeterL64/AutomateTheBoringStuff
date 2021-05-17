# Line Continuation

# Generally speaking, indentations in code tell Python that there is a block
# of code, and to treat it accordingly.

# However, you do not have to keep a line of code or lists all on one line.

# Lists can be written like this if you prefer for whatever reason:
spam = ['Apples',
        'Oranges',
        'Pears',
        'Bananas']
# Python is smart enough to realise you are still writing the list and doesn't
# create errors with each lines indentation.




# Suppose you are typing code and the code is longer than the Python window.
# You may want to continue the code on the next line rather than have the code
# continue past the window, which is quite annoying.
# Well, you can use the back slash, \ , key to tell Python you are continuing
# the code on the next line.
# The \ tells Python we are not starting a new block of code and
# to ignore any indentation

# Example:
print('Four score and seven' + \
      ' years ago.')
# Returns Four score and seven years ago.

print ('Four score and seven' + ' years ago.')
# Returns Four score and seven years ago.

# Both codes do the same thing, just that the backslash, \ , continues the
# code on the next line.

