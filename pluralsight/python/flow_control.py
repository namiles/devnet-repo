if True:
    print("It's true")

# Won't print
if False:
    print("It's true")

if bool("hello"):
    print("It's true")

if "hello":
    print("It's true")

if 11:
    print("11 is true!")

c = 5
while c != 0:
    print(c)
    c -= 1

#Infinite Loops
# while True:
#     pass

#Python does not support do..while or while..do loops. Must use While loops with breaks.
while True:
    response = input("Enter digits: ")
    if int(response) % 7 == 0:
        break

