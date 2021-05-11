# Chapter 1 Lesson 7
# You can use a while loop instead of a for loop if you like.


# While Loop
print('My name is')
i = 0
while i < 5:
    print('Jimmy Five Times ' + str(i))
    i = i + 1

# Both of these codes work. Delete one to run the program.

# For Loop
print('My Name Is')
for i in range(5):
    print('Jimmy Five Times ' + str(i))

# By using a for loop (second code) you don't have to write the lines "i=0"
# or "i = i+1".
# Here the "i" variable starts at 0 and ends at 4.
# Range starts at zero and is up to but not including the number.
# The for loop is more concise than the while loop.


print('My Name Is')
for i in range(12, 16):
    print('Jimmy Five Times ' + str(i))

# Here the range is set to (12, 16) which is from 12 up to but not including 16.
# So the output would be 12, 13, 14, 15.


print('My Name Is')
for i in range(0, 16, 2):
    print('Jimmy Five Times ' + str(i))

# Here the range is from 0 up to but not including 16, at intervals of 2.
# The output will start start at 0 ->    0, 2, 4, 6... 12, 14.


print('My Name Is')
for i in range(5, -1, -1):
    print('Jimmy Five Times ' + str(i))

# This code will start at 5 and count down to 0 (not including -1 remember) at
# intervals of -1.

