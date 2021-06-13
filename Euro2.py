# Euro Sweepstake

import random
import time


tier1 = ['France', 'Portugal', 'England','Germany', 'Belgium']
tier2 = ['Netherlands', 'Italy', 'Spain', 'Denmark', 'Croatia' ]
tier3 = ['Austria', 'Scotland', 'Wales', 'Poland','Switzerland']
tier4 = ['Ukraine', 'Turkey', 'Czech Rep.', 'Russia', 'Sweden']
tier = [tier1, tier2, tier3, tier4]

#print('Peters choices:')
#random1 = random.choice(tier1)
#random2 = random.choice(tier2)
#random3 = random.choice(tier3)
#random4 = random.choice(tier4)
#print(str(random1) + ' ' + str(random2) + ' ' + str(random3) + ' ' + (str(random4)))

#print()

#print('Davids choices:')
#rando1 = random.choice(tier1)
#if rando1 == random1:
#    rando1 =
#rando2 = random.choice(tier2)
#rando3 = random.choice(tier3)
#rando4 = random.choice(tier4)
#print(str(random1) + ' ' + str(random2) + ' ' + str(random3) + ' ' + (str(random4)))



print('In order: Peter, David, Nick, Luke, Phil')

new_tier = list(tier1)
random.shuffle(new_tier)
for a in new_tier:
    print(a)
    time.sleep(.6)

print()

new_tier = list(tier2)
random.shuffle(new_tier)
for b in new_tier:
    print(b)
    time.sleep(.6)

print()

new_tier = list(tier3)
random.shuffle(new_tier)
for c in new_tier:
    print(c)
    time.sleep(.6)

print()

new_tier = list(tier4)
random.shuffle(new_tier)
for d in new_tier:
    print(d)
    time.sleep(.6)


