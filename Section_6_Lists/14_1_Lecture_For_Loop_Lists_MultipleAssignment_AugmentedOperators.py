# Lesson 14 pg 86-88
# for Loops with Lists, Multiple Assignment, and Augmented Assignment Operators



for i in range(4): # A for loop repeats the code block once for value in a list
    print(i) # or a list-like value (eg range)
#Returns
#0
#1
#2
#3




# Range Objects and List-Like Values

range(4) # range function(4) returns a value thats of the data type: Range Object
#range(0,4) # Range Objects are List-Like values.
# Python considers the Range Object: range(0,4) to be the same as a list like
#[0,1,2,3]
# In fact, you could write the above for loop like this and get the same result;
for i in [0,1,2,3]:
    print(i)

# What Python is doing above is it takes the list value[0,1,2,3] and assigns the
# first item(0) to the variable i and run the block of code, then loop back and
# assign the second item in the list(1) to the variable i and run the block
# of code again, etc.







# The list() Function

# If you want to get the actual list value from a range object value, then you can
# just pass that to the list function and it will return an actual list for you.
range(4)
#range(0,4)
list(range(4))
#[0,1,2,3]

# This is handy if you need to get a collection of integers from a list. eg
list(range(0,100,2)) # Returns a list of integers from 0 up to but not including
                     # 100 in steps of 2.
# You can assign that list value to a variable, just like any other value:
spam = list(range(0,100,2))








# for i in range(len(SomeList))

# Use this code whenever you need to run loop code over a list where you need both
# the value inside of it and also the integer index.
# The list can be of any size and the same code will work.

supplies = ['pens', 'staples', 'pencils', 'mugs']
for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])
#Returns
#Index 0 in supplies is: pens
#Index 1 in supplies is: staples
#Index 2 in supplies is: pencils
#Index 3 in supplies is: mugs

# Code above is: We have a variable (supplies) that contains a list of string
# values.
# Then we have a for loop tht instead of just going through the range of something
# we will pass the range function the length(len) of supplies, and now we can
# use the "i" as an index for the supplies list inside this block of code.

# So using range, len, then the list, format inside of a for loop, we can then
# use the for loop vairable "i" to refer to both the integer Index of the list
# as we go through the loop, and use the list value with the index "i" to get
# the value inside the loop








# Multiple Assignment

cat = ['fat', 'orange', 'loud']
size = cat[0]
colour = cat[1]
disposition = cat[2]
# Three lines of code to assign each value within the list to a seperate variable.
# This is fine for small lists, but a list could be huge.

# A better way is using multiple assignment, which can be all one line.
# You can have multiple variables on the left side of an assignment
# operator "=", seperated by commas. And have a list value on the right side
# of the "=". eg below:
size, colour, disposition = cat
# Each variable on the  left is now assigned to the corresponding value in
# the list.


# Another way of using Multiple Assignment is to assign multiple vairables to
# multiple values all on the one line of code. Eh below:
size, colour, disposition = 'skinny', 'black', 'quiet'








# Swapping Variables

a = 'AAA'
b = 'BBB'
a,b = b,a # a is now assigned the value that b was originally assigned to.
          # Swapped the assignments.










# Augmented Assignment Operators


# A frequent thing to do with a variable is to use the variable itself
# to increment its value. eg:
spam = 42
spam = spam + 1
spam
#Returns 43

# A shortcut for this using Augmented Operators is
spam = 42
spam += 1
spam
#Returns 43

# There are Augmented operators for plus, minus, multiplication, division, and
# the modulus operators.
# Table below shows these:

# Augmented Assignment Statement        # Equivalent Assignment Statement
# spam += 1                             # spam = spam + 1
# spam -= 1                             # spam = spam - 1
# spam *= 1                             # spam = spam * 1
# spam /= 1                             # spam = spam / 1
# spam %= 1                             # spam = spam % 1