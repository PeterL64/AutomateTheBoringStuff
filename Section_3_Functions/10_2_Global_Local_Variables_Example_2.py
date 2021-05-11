spam = 42 # Global Variable                 #Global Scope

def eggs():                                 #Local Scope
    spam = 42 # Local Variable              #Local Scope

print('Some code here')                     #Global Scope
print('Some more code')                     #Global Scope

# A Scope is a container of variables. It can contain variables for the entire
# code in a program.
# The Global Scope is created when the program starts and is destroyed when
# the terminates.
# A Local Scope is created whenever a function is called, and all variables
# assigned during this function call exist within that Local Scope. When the
# function returns the Local Scope is destroyed and these variables are forgotten.


# Points to remember:
# 1) Code in the  Global Scope cannot use any Local Variables.
# 2) Code in the Local Scope can access Global Variables.
# 3) Code in one function's local scope cannot use variables in another local scope.
# 4) You can use the same name for different variables if they are in
#    different scopes.
