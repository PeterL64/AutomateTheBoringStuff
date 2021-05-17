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
