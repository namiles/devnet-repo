'''
File input and output

Modes
- r = open for reading (default)
- w = open for writing (overwrites)
- x = open for exclusive creation, failing if the file already exsits
- a = Open for writing, appending to the file if it exists

- b = Open in binary mode
- t = Open in text mode (default)
- + = Open for updating (read and write)

'''

#-------------------------------------------------------------#

# # Take file to open as a string and specify mode. readdata is an object created to store the contents of the file.
# readdata = open("textfile.txt", mode="r", encoding="utf-8")

# # read() can be used to print contents
# print()
# print(readdata.read())
# print()

# # When using open(), you have to close the file:
# readdata.close()

# # .readline() reads in only 1 line of the file at a time.
# print(" ** Read only the first line of the file:")
# my_file_object = open("textfile.txt", "r")
# print (my_file_object.readline())
# print (my_file_object.readline())
# my_file_object.close()

# # Reading one line a time using a loop
# print("** Read one line a time in a loop:")
# my_file_object2 = open("textfile.txt","r")
# x=1
# for line in my_file_object2:
#     print("Line " + str(x) + ":" + line)
#     x += 1
# my_file_object2.close()
# print()

#-------------------------------------------------------------#

'''
Keep track of opening and closing files can be annoying.
Python provides the with statement, also called a context manager. (with-blocks)
It uses the open() function but doesn't require assigning to an object and automatically closes the file.
'''

with open("textfile.txt", "r") as data:
    print("Data read using with statement:\n",data.read(), sep="")

# a+ can be used to write to the file by appending. 
with open("textfile.txt", "a+") as data:
    print(data.write("\nThis line was added using python."))

# Read file after adding the line.
with open("textfile.txt", "r") as data:
    print("\nData after writing to do:\n",data.read(), sep="")
print()

#-------------------------------------------------------------#