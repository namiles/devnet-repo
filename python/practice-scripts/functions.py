
# Functions
# - must not start with a number
# - must not be a reserved python word such as print, input, type, etc.
# - can be any combination of letters, numbers, underscores, or dashes.
# - create with the "def" keyword

# Create the function
def myFunction():
    '''Prints "hello my function"''' #First line of a function block, called a docstring - used to describe what a function does
    print("Hello my function")

print()
myFunction() # call the function
print()
help(myFunction) # see what a function does

def myAddition(arg1, arg2):
    sum = arg1 + arg2
    return sum # pass an arugment back to code that calls function

def mySub(arg1, arg2):
    result = arg1 - arg2
    return result

def sayHello(*args):
    for arg in args:
        print("hello ", arg,"!", sep="")

print(myAddition(5,5))
print()

# Keyword Arguments - used when arguments are not in consistent order
print(mySub(arg2=15, arg1=10))
print()

# Unknown amount of arguments - Functions can use * or ** (*args or *kwargs) to defiine a number of arguments or keyword arguments
sayHello("caleb", "nick", "erik", "justin")
