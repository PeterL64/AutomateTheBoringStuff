# The Dictionary Data Type

# Method 1
myDog = {'size':'big', 'colour':'white', 'disposition':'friendly'}
print(myDog['disposition'])
# Method 2
myCat = dict(size='fat', colour='grey', disposition='loud')
# This dictionary's keys are the strings 'size', 'colour', and 'disposition',
# And its values are 'fat', 'grey', and 'loud'
# This Dictionary is stored in the variable myCat

print(myCat['size'])


print('My cat has ' + myCat['colour'] + ' fur.')


spam = {12345: 'Safe Code', 24: 'room number'}

# Order matters for lists, but not for dictionaries.
# Eg this list will return False
print([1,2,3] == [3,2,1])
# This dictionary will return True
A = {'species':'cat','name':'Sleepy', 'age':5}
B = {'name':'Sleepy', 'age':5, 'species':'cat'}
print(A == B)
# Python considers these two dictionaries to be the same dictionary. Order does not matter.

# Think of the key-value pairs as word and drfinition pairs in a real dictionary.
# If you know the word, you can find the definition, or if you know the definition you can find the word.
# If you know the key, you can get the value.

# Trying to access a key which does not exist will return a key value error.
#print(A['colour']) # Will return a KeyError, since there is no 'colour' key in the dictionary A



# You can check if a key is in a dictionary with the "in" or "not in" operators.
print('name' in A)
print('name' not in A)



# Dictionaries are Mutable, as are lists. Variables hold references to dictionary values, not to that values themselves.




# There are three Dictionary Methods that will return List-Like values of the dictionary's keys, values or both keys and values
# These are:
print(list(A.keys()))
print(list(A.values()))
print(list(A.items())) # This returns two-item tuples









