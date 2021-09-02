# Python ceates an int object of 1000, and makes the variable x point to that object
x = 1000

# "Assigning" x to a new value does not change the int 1000 object, but creates a new int object and points x at it.
# Python garbage collector goes back and cleans up the old int 1000 object since it is no longer being refernced.
x = 500

# Assigned a variable that equals x creates another reference to int 500
y = x
# Changing x does not change y, and y continues to point at the int 500 objects
x = 100

print(y)
print(x)
