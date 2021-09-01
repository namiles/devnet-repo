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

# Bytes - similar to strings, but is a sequence of bytes rather than unicode codepoints
print(b'hello')
print(type(b'hello'))

# Lists - mutable, sequences of objects
list1 = [1,2,3]
list2 = ["apple", "orange", "banana"]
list3 = [1, "apple", {"name":"nick"}]
print(list3[2]["name"])

# Dicts - maps keys to values 
dict1 = {
    "key1":"value1",
    "key2":"value2",
}
print(dict1["key1"])

# for loops
colors = {'crimson':0xdc143c, 'coral':0xff7f50, 'teal':0x008080}
for color in colors:
    print(color, colors[color])