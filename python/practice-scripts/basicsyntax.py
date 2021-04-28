# single line comment

''' multi
    line   
    comment '''

print('hello world')
print() #blank line

#-------------------------------------------------------------#

# Variables
# - must start with a letter or underscore
# - cannot start with a number
# - can only consist of alphanumeric characters and underscores
# - case sensitive
# Variables are auto typed, meaning python sets it as a string, int, bool, etc automatically.

age = 23
name = "nick"
isTrue = True
print("Hi my name is " + name + " and I am " + str(age) + " years old and this is " + str(isTrue) + ".")
print()
print(type(name))

# Data Types
# - strings
# - ints
# - booleans
# - float
# - lists
# - tuples
# - dictionaires
# - sets


#-------------------------------------------------------------#

# Data Structures
# - Lists --> Python's alternative to arrays. Uses square brackets [ ] and are mutable.
# - Tuples --> Similar to lists but are immutable. Uses Parantheses ( )
# - Dictionaries --> Unordered data structure that uses curly braces { } with key-value pairs
#   - keys can only be immutable tpyes such as ints, strings, 
# - Sets --> Mutable, uses curely braces { } without key-value pairs.
#   - Frozen sets --> Immutable, uses curly braces { } but no key-value pairs like dictionairies.

mylist = ["apple", "orange", "banana", "pineapple", "mango"]
mytuple = ("skateboard", "bike", "scooter", "skates")
mydict = {"name":"nick", "age":23, "haircolor":"brown"}

print()
print(mylist)

#Lists can be edited since they are mutable
mylist.append("grapes")
print(mylist)
#Any element in a list can be accessed:
print(mylist[0]) #prints first item in list
print(mylist[0:3]) #prints first 3 items.

print()

print(mytuple)
print(mydict)

#-------------------------------------------------------------#

