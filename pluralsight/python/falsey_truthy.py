
# Bool() can be used to determine if an object is falsey, or truthy.

print("All intergers except for 0 are considered truthy.")
# Falsey
print(bool(0))
# Truthy
print(bool(225))

print("All floats except for 0.0 are considered truthy.")
# Falsey
print(bool(0.0))
# Truthy
print(bool(225.1))

print("Empty sets and lists are considered falsey, unless they contain objects")
# Falsey
print(bool([]))
print(bool(()))
# Truthy
print(bool(["apple"]))
print(bool(("banana")))
