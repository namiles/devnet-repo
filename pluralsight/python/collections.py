print("-" * 80)

# Strings - sequence of unicode codepoints
# Raw strings (what you see is what you get)
string1 = r'C:\Users\Merlin\Documents\Spells'
print(string1)

#Convert int to string
string2 = str(496)
print(string2)

# String functions - many available. view with help(str)
capitalized_string = str.capitalize("washington")
print(capitalized_string)

#Strings and be concatenated using +, += or .join method
high_string = 'High'
way_string = 'way'
man_string = 'man'
joined_string = ''.join([high_string,way_string,man_string]) # Notice how the strings to be joined are in a list - .join only takes one iterable argument
print(joined_string)

print("-" * 80)

# Bytes - similar to strings, but is a sequence of bytes rather than unicode codepoints
print(b'hello')
print(type(b'hello'))

print("\nLists",  "-" * 80)

##### Lists - mutable, sequences of objects #####
list1 = [1,2,3]
list2 = ["apple", "orange", "banana"]
list3 = [1, "apple", {"name":"nick"}]
print(list3[2]["name"])
# Negatives indexes are used to access the last objects in a list
print("Last object:",list2[-1])
print("Second to last object:",list2[-2])
# .index() function can be used to find location of an object in the list.
# Compares passed in object equivalence for each item in the list until is is equal
print(list2.index("orange"))


print("\nDicts", "-" * 80)

##### Dicts - maps keys to values #####
dict1 = {
    "key1":"value1",
    "key2":"value2",
}
# Values are accessible by keys
# Keys must be unique in a single dictionary
# Keys must be immutable
# Values can be immutable
# Order is not important in dicts
print(dict1["key1"])
#the dict constructor can be used to convert to dictionaries:
names_and_ages = [('Alice', 32), ('Bob', 24), ('Charlies', 42)]
print(names_and_ages)
converted_dict = dict(names_and_ages)
print(converted_dict)

print("\nTuples", "-" * 80)

##### Tuples - immutable sequences of objects, cannot be changed once created #####
# Tuples can contain any object
tuple1 = ("this", "this", "a", "tuple", 1)
print(tuple1)
print(tuple1[0])
print(tuple1[4])
print(len(tuple1))
for item in tuple1:
    print(item)
# To create a single element tuple, you must use a trailing comma
# If not used with ints, python will create an int, not a tuple
tuple2 = (746) #int
print("Tuple2 type:",type(tuple2))
tuple3 = (746,)
print("Tuple3 type:",type(tuple3))
empty_tuple = ()
print(type(empty_tuple))


print("\nSets", "-" * 80)

##### Sets - unordered collection of unique elements #####
# sets are mutable
# Elements in a set must be immutable
set1 = {6, 28, 496, 8128}
print(set1)
# Must uses set() constructor to create an empty set since dicts also use {}
not_a_set = {} # empty dict
print(type(not_a_set))
set2 = set() #empty set
print(type(set2))

print("-" * 80)

# for loops
colors = {'crimson':0xdc143c, 'coral':0xff7f50, 'teal':0x008080}
for color in colors:
    print(color, colors[color])

print("-" * 80)