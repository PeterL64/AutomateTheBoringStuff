# Deep Copy Example  --- import copy   copy.deepcopy()



spam = [0,1,2,3,4,5]
spam
# Returns [0, 1, 2, 3, 4, 5]
cheese = spam   # cheese now assigned the spam list
cheese[1] = 'Hello'
cheese
# Returns [0, 'Hello', 2, 3, 4, 5]
spam
# Returns [0, 'Hello', 2, 3, 4, 5]


# The reason both cheese AND spam change is because both don't necessarily copy
# the list we wrote out. They copy a reference to the list.
# Python creates a reference number that is assigned to produce the list whenever
# it is called upon. This is why changing a value in the cheese list also
# affects the value in the spam list. They are both refrencing the same source.

# To create a true copy of a list, follow steps below:


import copy


spam = [0, 1, 2, 3, 4, 5]
cheese = copy.deepcopy(spam) # Calling the copy Module's deepcopy Function & pass spam to it.
cheese[1] = 'Goodbye'
cheese
# Returns [0, 'Goodbye', 2, 3, 4, 5]
spam
# Returns [0, 1, 2, 3, 4, 5]


# We imported the copy Module, which has a function called deepcopy which can make
# a total copy of a list.
# deepcopy doesn't just copy the reference to a list, it creates a new version of
# the list and creates a new reference for this new list.

# Code above Explained:
# Created a list and assigned the variable spam to it.
# Called the copy Module's Function, deepcopy, and passed spam to it. This made
# a completely new copy of the spam list & we assigned the variable cheese to it.
# We changed the data at index 1, (index starts at 0 remember), and
# assigned it the new data, 'Goodbye'.
# We called the variable cheese and it produced our altered list.
# We called the variable spam and it produced the original list, unaltered.

# Technically speaking, once we copied spam, spam and cheese are two seperate
# lists that contain the same date. This is why we can alter each and not affect
# the other.


