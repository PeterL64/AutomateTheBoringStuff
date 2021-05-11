def spam():  # We define the function spam
    eggs = 'Hello' # We assign the value 'Hello' to the Local Variable eggs.
    print (eggs) # We print the Local Variable eggs

eggs = 42 # We assign the Global Variable eggs 42. Same name but different Variable
spam() # We call the Function spam, which assigns a Local Vairable and prints it.
print(eggs) # We print the Global Variable, eggs (42), which is different from
            # the Local Variable, eggs (Hello)




# You can make Python recognise the Local Variable as a Global Variable by adding
# this line to the Local scope.

def potatoe():
    global chips # Adding this line
    chips = 'Hello'
    print(chips)

chips = 44
potatoe()
print(chips)
