# This is a guess the number game.
import random
print('Hello. What is your name?')
name = input()
secretNumber = random.randint(1, 20) # Calls a random integer between and including 1 and 20 and stores it in the variable secretNumber.
print('Well, ' + name + ', I am thinking of a nummber between 1 and 20')

print('DEBUG: Secret Number is ' + str(secretNumber)) #This is for me to test if it is working. You wouldn't put this in the game.

# Ask the player to guess 6 times
for guessesTaken in range(1, 7): #You could use range(6), but better to have the actual ranges in the code.
    print('Take a guess.')
    guess = int(input()) #Input returns a string so we need to change to an integer.
    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    elif guess != (0, 20): # Code Error here
        print('Error: You must enter a number')
    else:
        break #This condition is the correct guess!

if guess == secretNumber:
    print('Good job ' + name + '! You have guessed my number in ' + str(guessesTaken) + ' guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber) + '.')

# BE CAREFUL OF PARENTHESIS, COMMAS, ETC. THEY CAN MESS UP YOUR CODE.
# I forgot a parenthesis at the end of the second last print statement and
# couldn't find it for ages.

# Remove the debug print if you were showing this to someone else.

