
# Functions
# - must not start with a number
# - must not be a reserved python word such as print, input, type, etc.
# - can be any combination of letters, numbers, underscores, or dashes.
# - create with the "def" keyword

# PEP 8 styling for functions
# - Lowercase with words separated by underscores
# - use one leading underscore for non-public methods and instance variables

# Create the function
def my_function():
    '''Prints "hello my function"''' #First line of a function block, called a docstring - used to describe what a function does
    print("Hello my function")

print()
my_function() # call the function
print()
help(my_function) # see what a function does

def my_addition(arg1, arg2):
    sum = arg1 + arg2
    return sum # pass an arugment back to code that calls function

def my_sub(arg1, arg2):
    result = arg1 - arg2
    return result

def say_hello(*args):
    for arg in args:
        print("hello ", arg,"!", sep="")

print(my_addition(5,5))
print()

# Keyword Arguments - used when arguments are not in consistent order
print(my_sub(arg2=15, arg1=10))
print()

# Unknown amount of arguments - Functions can use * or ** (*args or *kwargs) to defiine a number of arguments or keyword arguments
say_hello("caleb", "nick", "erik", "justin")
