def div42by(DivideBy):
    try:
        return 42 / DivideBy
    except ZeroDivisionError:
        print('Error: You tried to divide by zero.')

print(div42by(2)) # The program will try to divide by these numbers
print(div42by(12))
print(div42by(0)) # Here it tries to divide by 0, since the error shows up,
                  # the "except" statement runs and prints the string.
                  # Then since nothing is returned, the None value returns (since
                  # Python always returns something, if there is no value Python
                  # returns whats called the None Value.
print(div42by(1))


# When code in the try clause causes a ZeroDivisionError, the program execution
# immediately moves to the code inside the except clause

# Without the "try" and "except" statements, this program would crash and
# the error message ZeroDivisionError would display.
# With the "try" and "except" statements the program can run and not crash when
# mistakes or errors occur.


# You can also have a simple except statement without specifying the type of error
# it catches and it will catch all types of errors.
# This can be good for input validation.
def div44by(DivideBy):
    try:
        return 44 / DivideBy
    except:
        print('Error: You tried to divide by zero, you fool')

print(div44by(2))
print(div44by(12))
print(div44by(0))
