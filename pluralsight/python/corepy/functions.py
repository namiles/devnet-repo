import time

def sum(x, y):
    return x+y

print(sum(2,3))

# If no return is specified in a function, it returns an implicit "None", which does not display in the REPL
def no_return():
    print("This function has no return, but implicity returns None by python")

no_return()
(print(no_return() is None))


#Function Arguments - broder has a default argument of "-"
def banner(message, border="-"):
    line = border * len(message)
    print(line)
    print(message)
    print(line)

banner("This is a message")
#Positional Arguments, must be in order function expects
banner("This is a message", "#")
#Keyword arugments, can be supplied in any order. Keyword arguments must come after positional arguments though
banner("This is a message", border="*")
# OR
banner(border="=", message="This is a message")

print(time.ctime())
time.sleep(5)
print(time.ctime())