# Lesson 15 - List Methods, Pg 89 - 92

# METHODS

# 1
# A Method is basically a function.
# All list values have a Method called index()

spam = ['hello', 'hi', 'howdy', 'heya']
spam
# Returns the list inside spam
spam.index('hello') # Call the method on the list value spam
# Returns 0 because 'hello' is in the first position in the list.
spam.index('heya')
# Returns 3

# You can't call a method by itself, you have to call it for a list value.
# Eg below will not execute because Python does not know from what list you want
# to call the index 'hello' from. This is why we use the form above, not below.
index('hello')


# Each data type has their own set of methods.
# The list data type, for example, has methods for: finding, adding, removing
# and manipulating data within the list.



spam = ['Sleepy', 'Tiger', 'Abe', 'Tiger']
spam.index('Tiger')
# Returns 1
# For a list that has duplicate data inside it, and call the index method
# searching for the duplicated data, it will return only the first instance of
# the data, as shown above.
