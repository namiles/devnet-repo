'''
4 Types of scopes -- narrowest to broadest
local       Inside the current function
enclosing   Inside the enclosing functions
global      Top level of the module
build-in    Inside the builtins module
'''

count = 0

def show_count():
    print(count)

def set_count(c):
    global count
    count = c

# When functions cannot locate the object in the local scope, it goes up to the next --> enclosing --> global, etc
show_count()
#Setting the count does NOT set the object to 5 in the global scope, but will only set it in the function's local scope
set_count(5)
# You must add "global count" into the function if you want it to use the global scope
show_count()