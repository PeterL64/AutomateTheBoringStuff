# Lists and Strings Similarities. --- Mutable and Immutable Data Types


# 1

list('Hello')
# ['H', 'e', 'l', 'l', 'o']

name = 'Sophie'
name[0]
# 'S'
name[1:3}
# 'op'
name[-2]
# 'i'
'So' in name
# True
'xxx' in name
# False

for letter in name:
    print(letter)

# S
# o
# p
# h
# i
# e



# As you can see above, a string can be seen as a list of characters.


# However lists and strings are different in an important way.
# Lists are a Mutable data type. It can have values added, removed or changed.
# Strings are an Immutable data type, it cannot be changed.

# If you have a string, you can use indexing to access a letter in that string,
# but cannot change the string, like you would a list. Eg below:
name = 'Sophie the cat'
name[7]         # Accessing the letter
# 't'
name[7] = 'x'   # Changing the letter, not allowed
# Error

# If the above was a list data type and not a string:
name = [0, 1, 2, 3, 4, 5, 6]
name[2]
# 2
name[2] = 'Cat'
name
# [0, 1, 'cat', 3, 4, 5, 6]









# 2

# Creating new strings from slices

# The proper way to modify a string is to use a slice.


# So I have a string I wish to change the 'a' to 'the'.
name =  'Sophie a cat'
# We will have to create a new string, which we will store in a new variable.
# We will have to use slices to pick out the parts of the old string we wish
# to use in our new string and use string concatenation to add them together.
newName = name[0:7] + 'the' + name[8:12]
newName
# 'Sophie the cat'









# 3

# Differences between Mutable and Immutable Data types.



spam = 42
cheese = spam
spam = 100
spam
# 100
cheese
# 42


# When you assign a list to a variable, you are actually assigning a list
# reference to a variable.
# A reference is a value that points to some piece of data like, a list.
#
spam = [0, 1, 2, 3, 4, 5] # Say we assign this list to the variable, spam
cheese = spam # Now I want to assign the variable cheese the list, spam
cheese[1] = 'Hello' # Here we change the value at index 1
cheese
# [0, 'Hello', 2, 3, 4, 5]
spam
# [0, 'Hello', 2, 3, 4, 5]

# Here we see that spam also gets changed, even though we only wanted to change
# the value in the cheese variable.

# This is because Python created the original list, stored it, and when we
# assigned the variable, spam, to it, we actually didn't.
# What we did was assign spam to a REFERENCE to the list.
# So when we assigned cheese to the spam list, what we actually did was copy the
# reference to the same list.
# So when you modify the list that cheese is referencing to, you are also
# referencing the same list that spam is referencing to as well.



#3.5

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


