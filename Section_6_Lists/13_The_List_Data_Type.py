# The List Data Type Pg 79-87 Automate the Boring Stuff With Python Book

# A list is a value that contains values. The values are called items.
# They begin and end with square brackets [], and are delimited by commas(seperated).
# Eg
['cat', 'bat', 'rat', 'elephant']
# This is a list value that contains 4 values.
# You can assign it to a variable just like any other values.
# Eg
spam = ['cat', 'bat', 'rat', 'elephant']
spam # Calling spam produces the list value. (Try in interactive shell)



# In order to access an item inside a list, you use an integer index for the
# item's position in the list.
# The index also begins and ends with square brackets [].
# Eg
spam[0] # This is an index which evaluates to 'cat'. Remember 0 is the first item
        # in a list.
spam[2] # Evaluates to 'rat'.
spam[3] # Evaluates to 'elephant'.

# The process above is that spam evaluates to the list, then the index evaluates
# to the item it represents in the list.




# More examples
ValueName = [['cat', 'bat'], [10, 20, 30, 40, 50]]
ValueName[0] # Evaluates to ['cat', 'bat'], which is the first item in the list.
ValueName[0][1] # Evaluates to 'bat', the first item in the list, second in the
                # first item's list.



# You can use negative integers(numbers) for the index, which count from the end
# going backwards. Eg below:
spam[-1] # Evaluates to 'elephant'
ValueName[-1][-2] # Evaluates to 40.
'The ' + spam[-1] + ' is afraid of the ' + spam[-3] + '.'
# Evaluates to 'The elephant is afraid of the bat.'





# Slices
# A Slice will get several values from a list.
# A slice has two integer indexes seperated by a colon ":".
spam[1:3] # Evaluates to ['bat', 'rat']. It starts at the index 1 and goes up to
          # but not including index 3.
          # It is returned as a list of values. A brand new list.









# Changing list's items.

# You can assign a value to a variable like so:
spam = 'Hello' # Put the variable to the left side of the assignment operator. Spam now contains the string ' Hello'
spam # Returns 'Hello'

# You can do this inside lists as well with indexes and slices.
spam = [10, 20, 30]
spam[1] = 'Hello'
spam # Returns [10, 'Hello', 30]

# Adding a slice to a list
spam[1:3] = ['Cat', 'Dog', 'Mouse']
spam # Returns [10, 'Cat', 'Dog', 'Mouse']
     # Essentiallu replace the Two items at index 1 and 2, not including 3 (which is
     # outside the list) with Three new values.



# Slice Shortcuts
spam = ['cat', 'bat', 'rat', 'elephant']
spam[:2] # Leaving the first index blank tells Python to start at the beginning.
# Returns ['cat', 'bat']  Starts at beginning up to but not including index 2.

spam[1:] # Leaving the second index blank says to
# Returns ['bat', 'rat', 'elephant'] Starts at index 1 up to the end of the list.










# Deleting values from a list.
del spam[2] # Think of the del statement as the UNASSIGNMENT statement.
spam
# Returns ['cat', 'bat', 'elephant']
# Deletes the item at index 2 and everything after gets moved over,leaving no gap.
# Run it again and you get this result:
del spam[2]
spam
# Returns ['cat', 'bat']














# String and list Similarities.
# Think of a string value as a list of single character values.
# len function.
len('hello')
# Returns 5
len(1,2,3)
# Returns 3

# String concatination and list concatination.
'Hello' + 'World'
# Hello World
[1,2,3] + [4,5,6]
# [1,2,3,4,5,6]


# String replication and list replication.
'Hello' * 3
# 'HelloHelloHello'
[1,2,3] * 3
# [1,2,3,1,2,3,1,2,3]











# The list() Function
# This function returns values in a list format. Eg:
list('Hello')
# Returns ['H', 'e', 'l', 'l', 'o']







# If you need to determine if a value is or isn't in a list you can use the "in"
# and "not in" operators.
# Like other OPERATORS, the in and not in are used in expressions and
# "connect to" values.

# Here is a value that we are looking for, then the "in operator", and then the
# list value where it might be found.
'howdy' in ['hello', 'hi', 'howdy', 'heya']
# Evaluates to True

42 in ['hello', 'hi', 'howdy', 'heya']
# Evaluates to False

'howdy' not in ['hello', 'hi', 'howdy', 'heya']
# Evaluates to False











# To Recap:
# A list ia a value that contains multiple values.
# The values in a list are also called items.
# You can access items in a list with it's integer index.
# The indexes start at 0, not 1.
# You can also use negative indexes. -1 refers to the last item, -2 refers to the
# second last item, and so on.
# You can get multiple items from a list using a slice.
# Thee slice has two indexes. The new list's items start at the first index and
# go up to but doesn't include the second index.
# The len() function, concatenation, and replication work the same way with lists
# as they do with strings.
# You can convert a value into a list by passing it through the list() function.

