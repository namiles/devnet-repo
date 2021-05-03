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
# - can only consist of alphanumeric characters and underscores (a-z, A-Z, 0-9, _ underscores except for beginning, )
# - case sensitive
# - cannot use reserved words (False, None, True, and, as, assert, break, class, continue, def, del, elif, else, except, for, if, is, or, not, pass, return, etc.)
# Variables are auto typed, meaning python sets it as a string, int, bool, etc automatically.

age = 23
name = "nick"
isTrue = True
print("Hi my name is " + name + " and I am " + str(age) + " years old and this is " + str(isTrue) + ".")
print()
print(type(name))

# Immutable objects cannot have their values changed
# Mutable can be opened up and changed

# Data Types
# - strings: immutable
# - ints: immutable
# - booleans: immutable
# - float: immutable
# - lists: mutable
# - tuples: immutable
# - dictionaires: mutable
# - sets: mutable (frozen sets = immutable)

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
myset = {1,2,3,4,5,6,7,7}

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

print()
#-------------------------------------------------------------#

print("#------------------------------Input/Output-------------------------------#")

# Input and Output
# input() and print() are two essential python functions
# input() is used to get information from a user running the pyhon script
# print() is used to show output to a user's terminal
# ex: name = input("Enter your name: ")

#Output
print()
print("Hello world")
print("Hello\nWorld") #\n = new lines
print("numbers in myset:", myset) 
print("numbers in myset:", myset, sep="") #remove automatic single spaces between elements

#fstrings - used to create formatted text a lot faster
firstName = "Bob"
lastName = "Test"
print(f"My first name is {firstName} and my last name is {lastName}")

# #Input
# print()
# name = input("Enter your name: ")
# print("Your name is " + name)
# print(type(name))
# print()

# # Python stores every input as a string
# # In order to get a int or float, you must convert input 

# age = int(input("Enter your age: "))
# print(age)
# print(type(age))
# print()

# temp = float(input("Enter the temperature: "))
# print(temp)
# print(type(temp))
# print()

#-------------------------------------------------------------#

print()
print("#--------------------------Conditionals and Loops-------------------------#")

# Conditionals and Loops

# If statements = used to control flow basic on boolean logic
# print()
# score = int(input("Enter test score: "))

# if score >= 90:
#     print("Grade is A")
# elif score >= 80:
#     print("Grade is B")
# elif score >= 70:
#     print("Grade is C")
# elif score >= 60:
#     print("Grade is D")
# else:
#     print("Grade is F")

# For loops - Used to iterate a specific number of times, mostly used to iterate through data sets
print()
dataset = (1,2,3,4,5)
for i in dataset:
    print(i)

print()

# range() function can be used in for loops to iterate a specified amount of times
for i in range(3): 
    print(i) #starts at 0 by default

print()

for i in range(1,4):
    print(i)

print()

for i in range(0,101,10):
    print(i) #change increment to 10 and list 0-100

print()

# While loops - Used to loop as long as condition meets requirement.
# Main difference between while loops and for loops is that for loops are used to control interation, while loops are used to loop an unknown amount of times

count = 1

#loop until count is equal to 10.
while (count <= 10):
    print("Loop count is:", count)
    count+=1
else:
    print("Loop completed.")


#-------------------------------------------------------------#

print()
print("#--------------------------Numbers and Mathematics-------------------------#")

# Numbers and Mathematics

# Numeric Types
# - int:  whole numbers, no decimals
# - float: Decimal numbers
# - long: Only in python 2
# - complex:

# Number Ranges
# Python 2
#   - int limited to 32 bits - -2,147,483,648 - 2,147,483,648
#   - long limited to 64 bits - -9,223,372,036,854,775,808 - 9,223,372,036,854,775,80/
#
# Python 3
#   - int - can be any size, even greater than 64 bits
#   - No longs in python 3

# Notes:
# - When doing math with ints and floats, python 3 converts ints to floats as necessary
# - Python follows PEMDAS order when calculating

'''
Mathematics Operators
x + y: sum
x - y: subtraction
x * y: multiplication, product of x and y
x / y: Division, quotient of x and y
x // y: floored quotient, rounded down
x % y: Remainder of x/y
'''

var1 = 10
var2 = 6

print('\nMath Operators:')
print('Addition (+): ', var1, '+', var2, '=', var1+var2)
print('Subtraction (-): ', var1, '-', var2, '=', var1-var2)
print('Multiplication (*): ', var1, '*', var2, '=', var1*var2)
print('Division (/): ', var1, '/', var2, '=', var1/var2) # In python 2, result of division is always an integer compared to float in python 3
print('Truncating/Floor Division (rounds down) (//): ', var1, '//', var2, '=', var1//var2)
print('Modulo (remainder) (%): ', var1, '%', var2, '=', var1%var2)
print()

print(min(1,20,25,3)) #returns lowest number of given numbers
print(max(1,2,4,8,102)) #returns largest number of given numbers

# Decimal, Binary, and Hexadecimal Numbers
# - Integers are assumed to be decimal, or base 10
# - 0b = binary, 0x = hex, 0x = octal

#Hex = 1 2 3 4 5 6 7 8 9 A B C D E F

print()
print("Binary:",0b11100000)
print("Hex:",0xF)



#-------------------------------------------------------------#
