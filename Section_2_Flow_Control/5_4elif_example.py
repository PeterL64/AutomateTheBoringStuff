name = 'Bob'
age = 3000
if name == 'Alice':
    print('Hi, Alice')
elif age < 12:
    print('You are not Alice kiddo.')
elif age > 2000:
    print('You could be Alice')
elif age > 100:
    print('You more than likely are not Alice')

# This code would return "You could be Alice" because the first if statement
# was False. The first "else/if" statement was False. The second "else/if"
# statement was True. Since it was true the next "else/if" statement does not
# matter.


