# Euro Sweepstake

import random



tier1 = ['France', 'Portugal', 'England','Germany', 'Belgium']
tier2 = ['Netherlands', 'Italy', 'Spain', 'Denmark', 'Croatia' ]
tier3 = ['Switzerland', 'Turkey','Poland','Russia','Sweden']
tier4 = ['Ukraine', 'Austria', 'Czech Rep.', 'Wales', 'Scotland']
tier = [tier1, tier2, tier3, tier4]

print('The list is ' + str(tier))

def randtier1():
    random1 = random.choice(tier1)
    print(random1)
def randtier2():
    random2 = random.choice(tier2)
    print(random2)
def randtier3():
    random3 = random.choice(tier3)
    print(random3)
def randtier4():
    random4 = random.choice(tier4)
    print(random4)

def randp():
    randtier1()
    randtier2()
    randtier3()
    randtier4()

#print('Enter name:')
#name = input()
#print(str(name) + "'s" + " teams are " + str(randp()))


#for i in range(len(tier1)):
    #print(i)


lads = ['Peter', 'David', 'Luke', 'Nicholas', 'Philip']
print('Type your name')
name = input()
for attempts in range(4):
    if name in lads:
        print('Hello ' + name + '. Type a number between 1 and 4!')
    elif name not in lads:
        print('Try again and type your full first name!')
        name = input()
    else:
        break



randteam = random.choice(tier1)


for i in range(6):
    print('Type number between 1 and 4')
    number = int(input())
    if number != (1, 5):
        print('Pick a number between 1 and 4')
    #elif number > 0:
    #    print('Pick a number between 1 and 4 you wanker')
    else:
        print(randteam())


#for guessesTaken in range(1, 7): #You could use range(6), but better to have the actual ranges in the code.
#    print('Take a guess.')
#    guess = int(input()) #Input returns a string so we need to change to an integer.
#    if guess < secretNumber:
#        print('Your guess is too low.')
#    elif guess > secretNumber:
#        print('Your guess is too high.')
#    elif guess != (0, 20): # Code Error here
#        print('Error: You must enter a number')
#    else:
#        break #This condition is the correct guess!

#if guess == secretNumber:
#    print('Good job ' + name + '! You have guessed my number in ' + str(guessesTaken) + ' guesses!')
#else:
#    print('Nope. The number I was thinking of was ' + str(secretNumber) + '.')